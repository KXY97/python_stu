#!/usr/bin/python
#-*- coding:utf-8 -*-
import socket
while True:
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 直接发送请求
    host = ('127.0.0.1',8888)
    aaa = input('>>>')
    if aaa != 'exit':
        sock.sendto('aaa'.encode('utf-8'),host)
        msg = sock.recv(1024)
        print(msg.decode('utf-8'))
    else:
        break
    sock.close()