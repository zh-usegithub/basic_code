import socket
import json
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1',50000))
messg = clientSocket.recv(1024)
while True:
   user = input('请输入用户名：')
   password = input('请输入密码：')
   content = f'{user}|{password}'
   clientSocket.sendall(content.encode())
   reply = clientSocket.recv(1024)
   info = json.loads(reply.decode())
   if info["stat"]:
       print(info["msg"])
       break
   else:
        print(info['msg'])
clientSocket.close()

