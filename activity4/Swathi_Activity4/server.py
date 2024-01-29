import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 56789
server_socket.bind((host, port))
server_socket.listen()

print(f"Server listening on {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

while True:
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Client: {data}")

    message = input("Server: ")
    client_socket.send(message.encode('utf-8'))

    if data.lower() == "bye":
        break

client_socket.close()
server_socket.close()
