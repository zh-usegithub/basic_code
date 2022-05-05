import socket
import select
import time

client_list = []
for i in range(6):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)#设置为非阻塞
    try:
        client.connect(('127.0.0.1',50000))
    except Exception as e:
        pass
    client_list.append(client)
recv_list = []
while True:
    r,w,e = select.select(recv_list,client_list,[],0.1)#第二个参数表示，client_list中的任何一个socket对象连接成功，都会把此socket返回给w
    for socket in w:
        socket.sendall('我已连接成功，请向我返回数据'.encode())
        recv_list.append(socket)
        client_list.remove(socket)
    for socket in r:
        data = socket.recv(1024)
        print(f'服务器返回数据:{data.decode()}')
        recv_list.remove(socket)
    if not recv_list and not client_list:
        break


