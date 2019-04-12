#!/usr/bin/python
#-*- coding:utf-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
server = 'smtp.163.com'
from_user = '13782826564@163.com'
res = '1872123622@qq.com'
passwd = 'zxc000'   # 授权码，允许登录客户端的密码
message = email.mime.multipart.MIMEMultipart()   # 创建空邮件
message['From'] = from_user    # 邮件的发件人
message['To'] = res   # 邮件的接收者
message['Subject'] = 'python_python'   # 邮件主题
text = """
哈哈哈哈哈
2019年
星期五
哈哈哈哈哈
"""
tex = email.mime.text.MIMEText(text,'plain','utf-8')   # 对正文进行编码
message.attach(tex)   # 将正文添加到邮件中
att = email.mime.text.MIMEText(open('11.jpg','rb').read(),'base64','utf-8')   # 对附件进行读取和编码
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment;filename="11.jpg"'   # 给附件添加头部信息
message.attach(att)   # 将附件添加到邮件里
smtp123 = smtplib.SMTP_SSL(server,465)   # 登录服务器
smtp123.login(from_user,passwd)
smtp123.sendmail(from_user,res,message.as_string())   # 发送邮件
smtp123.close()