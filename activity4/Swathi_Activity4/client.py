import socket

# Creating a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server's address and port
host = '127.0.0.1'
port = 56789
client_socket.connect((host, port))

while True:
    # Sending a message to the server
    message = input("Client: ")
    client_socket.send(message.encode('utf-8'))

    # Receiving a response from the server
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Server: {data}")

    # Checking if the server wants to terminate the conversation
    if data.lower() == "bye":
        break

# Closing the connection
client_socket.close()
