import socket
import struct

class NetError(Exception):
    pass

class Utils:
    @classmethod
    def addr_to_bytes(cls, address: tuple[str, int]):
        ip, port = address
        ip_bytes = socket.inet_aton(ip)             # 4 bytes
        port_bytes = struct.pack('!H', port)        # 2 bytes, network byte order (big-endian)
        return ip_bytes + port_bytes                # 6 bytes total

    @classmethod
    def bytes_to_addr(cls, data: bytes):
        if len(data) != 6:
            raise NetError(f"Invalid addr length {len(data)}, data: {data}")
        ip, port = data[:4], data[4:]
        ip_str = socket.inet_ntoa(ip)               # 4 bytes
        port_str = struct.unpack('!H', port)[0]     # 2 bytes, network byte order (big-endian)
        return ip_str, port_str                     # 6 bytes total