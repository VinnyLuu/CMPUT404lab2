import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8001              # Arbitrary non-privileged port

def handle_connection(conn, addr):
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print('Received', repr(data))
            if not data: break
            conn.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        p = Process(target=handle_connection, args=(conn, addr))
        p.start()
        p.join()