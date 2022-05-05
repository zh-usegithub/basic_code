import socket
dataSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dataSocket.connect(('127.0.0.1',50000))#向指定IP发送连接请求
message = dataSocket.recv(1024)#获取服务器发送信息
print(message.decode())
while True:
    content = input('请输入内容【Q退出当前连接】')
    if content.upper() =='Q':
        break
    dataSocket.sendall(content.encode())
    reply = dataSocket.recv(1024)
    print(reply.decode())
dataSocket.close()#关闭连接，自动向服务端发送空数据


