import os
import socket
import time

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1',50000))
while True:
    file_path = input('请输入要上传的文件路径：')
    file_size = os.stat(file_path).st_size#使用os模块下的方法计算文件的大小
    clientsocket.sendall(str(file_size).encode('utf-8'))#向服务端发送要上传的文件大小
    print('准备上传......')
    time.sleep(2)
    print('开始上传')
    file_object = open(file_path,mode='rb')
    read_size = 0
    while True:
        send_object = file_object.read(1024)
        clientsocket.sendall(send_object)
        read_size +=len(send_object)
        if read_size == file_size:
            break
clientsocket.close()




