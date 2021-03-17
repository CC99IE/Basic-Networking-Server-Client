import socket

connection = 1

HOST = input("IP: ") # 127.0.0.1 
PORT = int(input("Port: ")) # 8080


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while connection == 1:
        message = input("Message: ")
        s.sendall(bytes(message, 'utf-8'))
        data = s.recv(1024)
        print('Received', repr(data))
        connection = int(input("Do you want to send another message?(0/1) "))
        if connection == 0:
            s.close()