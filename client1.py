# -*- coding: utf-8 -*-

import socket


ip_port = ('172.28.156.205', 20001)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data = sk.recv(1024)
    print 'receive:', data
    inp = raw_input('please input:')
    sk.sendall(inp)
    if inp == 'exit':
        break

sk.close()
