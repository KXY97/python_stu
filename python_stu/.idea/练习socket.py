#!/usr/bin/python
#-*- coding:utf-8 -*-
import socket
# 创建一个套接字,规定使用tcp协议，IP版本
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定IP地址，端口号，接收的是个元组
s.bind(('127.0.0.1',8888))
# 监听服务是否开启，数字指的是最大等待数字
s.listen(3)
while True:
    # 接收请求
    # 第一个是连接信息，第二个是客户端的IP和端口号
    conn,addr = s.accept()
    # 接收数据,1024表示一次性最大能够接收1024字节的数据
    reg = conn.recv(1024)
    print(reg.decode('utf-8'))
    msg = input('>>>')
    if msg != 'exit':
        conn.send(msg.encode('utf-8'))
    else:
        break