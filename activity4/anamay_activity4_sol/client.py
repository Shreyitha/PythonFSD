'''
This is the client side of the code 
First we need to run the server.py than we need to run this file.
written by - Anamay Dubey
Date - 29/01/24
'''
import socket

def client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client_socket.connect(('localhost', 999))
    print("Connected to the Server")
    while True:
        # Send data to server
        message = input('Client: ')
        client_socket.send(bytes(message, 'UTF-8'))  # Corrected encoding

        # Receive response from server
        response = client_socket.recv(1024).decode()
        print('Server:', response)

        if message.lower() == 'bye': #break loop id message says 'bye'
            break

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    client()
