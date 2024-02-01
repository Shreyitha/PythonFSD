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

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

while True:
    message = input("Enter your message (type 'bye' to exit): ")
    client_socket.send(message.encode('utf-8'))

    if message.lower() == 'bye':
        break

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {response}")

client_socket.close()