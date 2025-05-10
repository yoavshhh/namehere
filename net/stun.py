import os
import struct

STUN_SERVERS = [
    ""
]

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
    
