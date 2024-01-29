import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server's address and port
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))

while True:
    # Send a message to the server
    message = input("Client: ")
    client_socket.send(message.encode('utf-8'))

    # Receive a response from the server
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Server: {data}")

    # Check if the server wants to terminate the conversation
    if data.lower() == "bye":
        break

# Close the connection
client_socket.close()
