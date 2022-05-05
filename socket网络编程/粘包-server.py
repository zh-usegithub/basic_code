import socket
import struct
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('127.0.0.1',50000))
socket.listen(6)
while True:
    conn,addr = socket.accept()
    print(f'接收到连接{addr}')
    while True:
        #读取固定的4字节数据
        header1 = conn.recv(4)
        if header1:
            data_length1 = struct.unpack('i',header1)[0]#计算长度
            has_recv_len = 0
            data1 = b''
            while True:
                length = data_length1-has_recv_len
                if length > 1024:
                    lth = 1024
                else:
                    lth = length
                chunk = conn.recv(lth)
                data1+=chunk
                has_recv_len+=len(chunk)
                if has_recv_len == data_length1:
                    break
            print(data1.decode())
        else:
            break




# header2 = conn.recv(4)
# data_length2 = struct.unpack('i',header2)[0]
# data2 = conn.recv(data_length2)
# print(data2.decode())
conn.close()
socket.close()


