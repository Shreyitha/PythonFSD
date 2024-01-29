import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {host}:{port}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Client: {data}")

    # Send a response to the client
    message = input("Server: ")
    client_socket.send(message.encode('utf-8'))

    # Check if the client wants to terminate the conversation
    if data.lower() == "bye":
        break

# Close the connection
client_socket.close()
server_socket.close()
