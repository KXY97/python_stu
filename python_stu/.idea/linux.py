#!/usr/bin/python
#-*- coding:utf-8 -*-
import paramiko
# 创建一个远程客户端
ssh123 = paramiko.SSHClient()
# 允许连接不在know_host文件中的主机
ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh123.connect(hostname='192.168.0.60',
               port=22,
               username='root',
               password='123456')
# # exec_command 执行命令 直接具有结果的命令
# # while True:
# #     qq=input('请输入')
# #     if qq != 'exit':
# #         a,b,c = ssh123.exec_command('qq')
# #         print(b.read().decode())
# #     else:
# #         break
# # # 第一个变量是表示输入的命令
# # # 第二个变量是命令执行的结果
# # # 第三个变量是命令的报错
# # ssh123.close()