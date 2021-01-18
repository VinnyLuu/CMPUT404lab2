import socket

# sources used: https://docs.python.org/3/library/socket.html
# how to send an http request: https://stackoverflow.com/questions/34192093/python-socket-get
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("www.google.com", 80))
    s.sendall(bytearray("GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n", 'utf-8'))
    data = s.recv(1024)
print('Received', repr(data))
