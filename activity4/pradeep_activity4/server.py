import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 690

server.bind((host, port))

server.listen()

print('Server is waiting for the request on {} : {}'.format(host, port))

client, address = server.accept()
print('Connected by', address)

while True:
    data = client.recv(1024).decode()

    if data.lower() == 'bye':
        print("Clinet has terminated the connection.")
        break

    print(f"Recived request from client : {data}")

    message = input("Enter your response: ")
    client.send(message.encode())

client.close()
server.close()
