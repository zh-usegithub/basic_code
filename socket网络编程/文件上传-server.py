import socket
listensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listensocket.bind(('127.0.0.1',50000))
listensocket.listen(5)
conn,addr = listensocket.accept()
print(f'接收到来自{addr}的连接')
data = conn.recv(1024)
totle_file_size = int(data.decode('utf8'))#计算接收文件的大小
file_object = open('savedata.png','wb')
recv_size = 0
while True:
    print('等待文件上传......')
    while True:
        data = conn.recv(1024)#服务器每次最多接收1024字节，但是可能每次接收到的数据是小于1024字节的
        file_object.write(data)
        file_object.flush()
        recv_size+=len(data)
        if recv_size == totle_file_size:
            break
    print('文件接收完成')
conn.close()
listensocket.close()


