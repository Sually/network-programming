# -*- coding: utf-8 -*-

import socket
import threading
import select


def process(request, client_addr):
    print request, client_addr
    coon = request
    coon.sendall('welcome to 10086!')
    flag = True
    while flag:
        data = coon.recv(1024)
        if data == 'exit':
            flag = False
        elif data == '0':
            coon.sendall('通过可能会被录音！')
        else:
            coon.sendall('please type again')

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind(('127.0.0.1', 20001))
s1.listen(5)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.bind(('127.0.0.1', 20002))
s2.listen(5)

while True:
    r, w, e = select.select([s1, s2, ], [], [], 1)
    for s in r:
        print 'get request'
        request, client_address = s.accept()
        t = threading.Thread(target=process, args=(request, client_address))
        t.daemon = False
        t.start()

s1.close()
s2.close()
