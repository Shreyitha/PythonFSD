import socket

host='localhost'
port=4000
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print('Waiting for client to connect')
client, addr= server.accept()
print("My client is from:", str(addr))
while True:
    message= client.recv(1024).decode('utf-8')
    print('Client: ', message)

    if message.lower()== 'bye':
        break

    response= input('Server:')
    client.send(response.encode('utf-8'))

client.close()
server.close()    
