import socket
from multiprocessing import Pool

def connect(x):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((x[0], x[1]))
        s.sendall(bytearray("GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n", 'utf-8'))
        data = s.recv(1024)
    print('Received', repr(data))
    s.close()

# TEST CODE
HOST = "127.0.0.1"
PORT = 8001
a = [(HOST, PORT)]
with Pool() as p:
    p.map(connect, a * 10)

