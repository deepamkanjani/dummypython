#!/usr/bin/python
__author__ = 'deepam'


from pyfuzz.generator import *
import socket

msg = b"GET " + random_ascii() + b" HTTP/1.1\nHost: 172.30.42.114\r\n"
print(msg)

try:
    s = socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("172.30.42.114", 80)
    s.connect(addr)
    s.sendall(msg)
    resp = s.recv(4096)
    print(resp)
except Exception as e:
    print(e)
finally:
    s.close()