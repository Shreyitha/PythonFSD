#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SONIYA JAIN
#
# Created:     01-02-2024
# Copyright:   (c) SONIYA JAIN 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))
server_socket.listen()

print(f"Server is listening on {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

while True:
    data = client_socket.recv(1024).decode('utf-8')

    if data.lower() == 'bye':
        break

    print(f"Received from client: {data}")

    response = input("Enter your response: ")
    client_socket.send(response.encode('utf-8'))

client_socket.close()
server_socket.close()
