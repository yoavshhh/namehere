import sys
import logging
import socket
import struct
import platform
import base64
from threading import Event, Thread
from collections import namedtuple

from net.stun import StunClient
from net.utils import Utils

class Peer:
    STOP = Event()
    def __init__(self):
        self.stun = StunClient()
        self.sock, self.code = self.peercode()
        logging.info(f"Code: {self.code}")
        self.connect()
    
    def connect(self):
        
        othercode = base64.b64decode(input("Peer code: ").encode())
        other_prv_addr = Utils.bytes_to_addr(othercode[:6])
        other_pub_addr = Utils.bytes_to_addr(othercode[6:])

        threads = {
            '0_accept': Thread(target=self.try_accept, args=(self.prv_addr[1],)),
            # '1_accept': Thread(target=self.accept, args=(client_pub_addr[1],)),
            '2_connect': Thread(target=self.try_connect, args=(self.prv_addr, other_prv_addr,)),
            '3_connect': Thread(target=self.try_connect, args=(self.prv_addr, other_pub_addr,)),
        }
        for name in sorted(threads.keys()):
            logging.info('start thread %s', name)
            threads[name].start()

        while threads:
            keys = list(threads.keys())
            for name in keys:
                try:
                    threads[name].join(1)
                except TimeoutError:
                    continue
                if not threads[name].is_alive():
                    threads.pop(name)
    
    def peercode(self):
        sock, response = self.stun.send_binding_requests()
        self.prv_addr = sock.getsockname()
        self.pub_addr = response.get_address()
        codebytes = Utils.addr_to_bytes(self.prv_addr) + Utils.addr_to_bytes(self.pub_addr)
        code = base64.b64encode(codebytes).decode()
        return sock, code

    def try_accept(self, port):
        logging.info("accept %s", port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if platform.system() == "Linux":
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        s.bind(('', port))
        s.listen(1)
        s.settimeout(5)
        while not Peer.STOP.is_set():
            try:
                conn, addr = s.accept()
            except socket.timeout:
                continue
            else:
                logging.info("Accept %s connected!", port)
                Peer.STOP.set()

    def try_connect(self, local_addr, addr):
        logging.info("connect from %s to %s", local_addr, addr)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if platform.system() == "Linux":
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        s.bind(local_addr)
        while not Peer.STOP.is_set():
            try:
                s.connect(addr)
            except socket.error:
                continue
            # except Exception as exc:
            #     logging.exception("unexpected exception encountered")
            #     break
            else:
                logging.info("connected from %s to %s success!", local_addr, addr)
                Peer.STOP.set()

    def send(self, data, target):
        self.socket.sendto(data.encode(), target)

    def receive(self):
        data, addr = self.socket.recvfrom(1024)
        return data.decode(), addr