import socket
import json
listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSocket.bind(('127.0.0.1',50000))
listenSocket.listen(6)
print('等待客户端进行连接')
while True:
    coonSocket,addr = listenSocket.accept()
    print(f'接收到客户端{addr}')
    coonSocket.sendall('欢迎使用登录认证系统'.encode())
    while True:
        data = coonSocket.recv(1024)
        if not data:
            break
        data_string = data.decode('utf-8')
        username,password = data_string.split('|')
        print(username,password)
        file_object = open('db.csv',mode='r',encoding='utf-8')
        sign = False
        for line in file_object:
            user,pwd = line.strip().split(',')
            print(user,pwd)
            if user == username and  pwd == password:
                print('qweqew')
                sign = True
                print('now',sign)
        file_object.close()
        print(sign)
        if sign:
            info = {"stat":True,"msg":"登录成功"}
            coonSocket.sendall(json.dumps(info).encode())
            break
        else:
            info = {"stat": False, "msg": "登录失败"}
            coonSocket.sendall(json.dumps(info).encode())
    coonSocket.close()
listenSocket.close()


