import socket

HOST = "127.0.0.1"
PORT = 8001
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytearray("GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n", 'utf-8'))
    data = s.recv(1024)
print('Received', repr(data))
s.close()