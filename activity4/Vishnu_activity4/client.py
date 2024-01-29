import socket as skt

server_address = ('localhost', 2024)

client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

client_socket.connect(server_address)
print("Connected to the server!")

while True:

    message = input("Enter message: ")
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")

    if message.lower() == 'bye':
        break

client_socket.close()