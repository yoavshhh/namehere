import os
import struct
import logging
import socket

STUN_SERVERS = [
    "stunserver2025.stunprotocol.org:3478"
]

class StunError(Exception):
    pass

class StunBindingRequest:
    BINDING_REQUEST = 0x0001
    MAGIC_COOKIE = 0x2112A442

    def __init__(self):
        self.transaction_id = os.urandom(12)

    def build(self):
        msg_type = self.BINDING_REQUEST
        msg_length = 0  # No attributes
        magic_cookie = self.MAGIC_COOKIE

        # Pack header: type (2 bytes), length (2), magic cookie (4), transaction ID (12)
        header = struct.pack(
            '!HHI12s',
            msg_type,
            msg_length,
            magic_cookie,
            self.transaction_id
        )
        return header

    def to_bytes(self):
        return self.build()

class StunBindingResponse:
    MAGIC_COOKIE = 0x2112A442

    def __init__(self, data):
        self.data = data
        self.transaction_id = data[8:20]
        self.ip = None
        self.port = None
        self._parse()

    def _parse(self):
        msg_type, msg_len, magic_cookie = struct.unpack('!HHI', self.data[:8])
        if msg_type != 0x0101 or magic_cookie != self.MAGIC_COOKIE:
            return  # Not a Binding Response or bad magic cookie

        attr_start = 20
        while attr_start < 20 + msg_len:
            attr_type, attr_len = struct.unpack('!HH', self.data[attr_start:attr_start+4])
            attr_value = self.data[attr_start+4:attr_start+4+attr_len]

            if attr_type == 0x0020:  # XOR-MAPPED-ADDRESS
                self._parse_xor_mapped_address(attr_value)
                break

            # 4-byte alignment
            attr_start += 4 + ((attr_len + 3) & ~3)

    def _parse_xor_mapped_address(self, value):
        _, family = struct.unpack('!BB', value[:2])
        xport = struct.unpack('!H', value[2:4])[0] ^ (self.MAGIC_COOKIE >> 16)

        if family == 0x01:  # IPv4
            xip = struct.unpack('!I', value[4:8])[0] ^ self.MAGIC_COOKIE
            self.ip = socket.inet_ntoa(struct.pack('!I', xip))
            self.port = xport

    def get_address(self):
        return (self.ip, self.port)
    
class StunClient:
    def __init__(self, servers=STUN_SERVERS, timeout=4):
        self.servers = servers
        self.timeout = timeout

    def send_binding_requests(self):
        request = StunBindingRequest().to_bytes()

        for server in self.servers:
            host, port = server.split(':')
            port = int(port)

            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.timeout)
                sock.connect((host, port))
                sock.send(request)
                logging.debug(f"Sent to {host}:{port}")
                
                response = sock.recv(1024)
                logging.debug(f"Received {len(response)} bytes from {host}:{port}")
                return sock, StunBindingResponse(response)
            except socket.timeout:
                logging.debug(f"Timeout from {host}:{port}")
            except Exception as e:
                logging.debug(f"Error with {host}:{port} - {e}")
        raise StunError("No stun server found")