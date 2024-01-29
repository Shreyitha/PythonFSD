import socket
host = 'localhost'
port = 4000
t = (host,port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(t)
s.listen(1)
server, addr= s.accept()
print("My client is from:", str(addr))
while True:
    message_from_client = c.recv(1024)
    if  message_from_client == 'bye' :
        break
    print("client says:", str(message_from_client.decode('utf-8')))
    message_to_client = input("Enter Response: ")
    server.send(message_to_client.encode('utf-8'))
server.close()