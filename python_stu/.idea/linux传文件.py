#!/usr/bin/python
#-*- coding:utf-8 -*-
# import paramiko
# # 建立一个传输通道
# ssh123 =paramiko.Transport('192.168.0.60',22)
# # 连接linux
# ssh123.connect(username='root',password='123456')
# # 创建一个传输文件的对象
# sftp = paramiko.SFTPClient.from_transport(ssh123)
# # 从Linux到Windows传输文件
# # 第一个参数表示要传输的文件
# # 第二个表示存放的本机位置
# sftp.get('install.log',r'.\abc.log')
# ssh123.close()

import paramiko
ssh123 =paramiko.Transport('192.168.0.60',22)
ssh123.connect(username='root',password='123456')
sftp = paramiko.SFTPClient.from_transport(ssh123)
sftp.put('a.txt',r'/home/a.txt')
ssh123.close()