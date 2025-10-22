from ctypes import *
import socket
import struct

# realization through Ctypes
class IP_ctypesStyle(Structure):
    _fields_ = [
        ("ihl", c_ubyte, 4), # 4-bit unsign char type
        ("version", c_ubyte, 4), # 4-bit unsign char type
        ("tos", c_ubyte, 8), # 1-byte unsign char type (type of service)
        ("len", c_ushort, 16), # 2-byte unsign short type
        ("id", c_ushort, 16), # 2-byte unsign short type
        ("offset", c_ushort, 16), # 2-byte unsign short type
        ("ttl", c_ubyte, 8), # 1-byte unsign char type (time to live)
        ("protocol_num", c_ubyte, 8), # 1-byte unsign char type
        ("sum", c_ubyte, 16), # 2-byte unsign short type
        ("src", c_ubyte, 32), # 4-byte unsign int type
        ("dst", c_ubyte, 32), # 4-byte unsign int type
    ]
    def __new__(cls, socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        # human readable IP addresses
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))


# realization through Class
class IP_structStyle:
    def __init__(self, buff=None):
        header = struct.unpack('<BBHHHBBH4s4s', buf)
        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xF

        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]

        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)

        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}