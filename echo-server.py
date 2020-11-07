#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 6332        # Port to listen on (non-privileged ports are > 1023). port should be an integer from 1-65535 (0 is reserved)

# socket.socket() creates a socket object that supports the context manager type, 
# so you can use it in a with statement. There’s no need to call s.close():
#AF_INET,specify the address family and socket type (IPv4)
#SOCK_STREAM is the socket type for TCP
#listen()It specifies the number of unaccepted connections that the system will allow before refusing new connections.
#accept() blocks and waits for an incoming connection.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)