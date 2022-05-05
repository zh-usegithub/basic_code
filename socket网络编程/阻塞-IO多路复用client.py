import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',50000))
while True:
    content = input('>>')
    if content.upper() == 'Q':
        break
    client.sendall(content.encode())
client.close()
