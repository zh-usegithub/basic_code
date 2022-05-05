import socket
import struct
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',50000))
data1 = 'hello,server'.encode()
header1 = struct.pack('i',len(data1))
client.sendall(header1)
client.sendall(data1)

data1 = 'this is client'.encode()
header1 = struct.pack('i',len(data1))
client.sendall(header1)
client.sendall(data1)
client.close()


