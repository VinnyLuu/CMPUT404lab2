from multiprocessing import Process
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8001              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            client_data = conn.recv(1024)
            print('Received from client', repr(client_data))
            if not client_data: break
            # connect with google and send recieved data to google
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as google_s:
                google_s.connect(("www.google.com", 80))
                google_s.sendall(client_data)
                google_data = google_s.recv(1024)
            print('Received from google', repr(google_data))

            conn.sendall(google_data)