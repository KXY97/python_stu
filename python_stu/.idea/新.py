import socket
while True:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接服务器
    sock.connect(('127.0.0.1',8888))
# send发送请求
    reg = input('>>>')
    if reg != 'exit':
        sock.send(reg.encode('utf-8'))
# 接收数据
        msg = sock.recv(1024)
        print(msg.decode('utf-8'))
    else:
        break
sock.close()