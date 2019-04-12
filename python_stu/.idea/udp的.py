#!/usr/bin/python
#-*- coding:utf-8 -*-
import socket
# 创建一个套接字,规定使用tcp协议，IP版本
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定IP地址，端口号，接收的是个元组
s.bind(('127.0.0.1',8888))
while True:
    # 第一个变量是客户端发送的请求数据，第二个变量是客户端的IP和端口号
    conn,addr =s.recvfrom(1024)
    # 打印接收数据
    print(conn.decode('utf-8'))
    # 发送响应s.sendto('响应的数据','客户端的IP地址和端口号')
    bbb = input('>>>')
    if bbb != exit:
        s.sendto('bbb'.encode('utf-8'),addr)
    else:
        break