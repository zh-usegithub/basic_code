import select
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',50000))
server.listen(6)
inputs = [server,]
while True:
    r,w,e = select.select(inputs,[],[],0.05)
    for socket in r:
        if socket == server:
            coon,addr = socket.accept()
            print(f'接收到新的连接{addr}')
            inputs.append(coon)#把客户端连接的socket放进inputs列表里面
        else:
            data = socket.recv(1024)
            if data:
                print(f'收到消息:{data.decode()}')
                socket.sendall('我已收到你的消息，现在返回信息'.encode())
            else:
                print('关闭连接')
                inputs.remove(socket)#把此次客户端连接过来的socket移除列表