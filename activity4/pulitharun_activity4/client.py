import socket
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 4000
client.connect((host, port))
print("Connected to the server")
while True:
    message_to_server = input("Enter your message: ")
    client.send(message_to_server.encode('utf-8'))
    if message_to_server == "bye":
        break
    message_from_server = s.recv(1024).decode('utf-8')
    print("Message From Server:", str(message_from_server))
client.close()
