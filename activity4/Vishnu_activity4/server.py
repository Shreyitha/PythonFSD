import socket as skt

server_address = ('localhost', 2024)

server_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

server_socket.bind(server_address)

server_socket.listen()
print("Waiting for connection!")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Client request: {data}")
    
    if data.lower() == 'bye':
        client_socket.send("connection closed as per the client request!".encode('utf-8'))
        break
    else:
        response = input("Enter response: ")
        client_socket.send(response.encode('utf-8'))

client_socket.close()
server_socket.close()