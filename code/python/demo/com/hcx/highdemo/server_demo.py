#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

s = socket.socket()
host = socket.gethostname()
port = 15565
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print(addr)
    c.send('welcome test'.encode())
    c.close()
