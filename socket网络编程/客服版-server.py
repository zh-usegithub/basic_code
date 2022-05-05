import socket
lisensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#创建一个socket套接字
lisensocket.bind(('127.0.0.1',50000))#监听本机的IP和端口号
lisensocket.listen(5)#表示最多同时接受5个连接
while True:
    dataSocket,addr = lisensocket.accept()#等待连接，这是一个阻塞操作
    print(f'接收到一个连接{addr}')
    dataSocket.sendall('欢迎使用客服系统，输入您想要办理的业务'.encode())
    while True:
        data = dataSocket.recv(1024)#等待接收消息
        if not data:
            break
        data_string = data.decode()
        print(f'接收到消息{data_string}')
        dataSocket.sendall('你说啥'.encode())
    print('与当前客户端断开连接')
    dataSocket.close()#关闭与此客户端的连接
lisensocket.close()#停止服务端程序



