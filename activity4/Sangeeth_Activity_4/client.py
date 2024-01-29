import socket

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',4000))
print('Connected to the server')

while True:
    message= input('Client: ')
    client.send(bytes(message, 'UTF-8'))

    if message.lower()=='bye':
        break

    response= client.recv(1024).decode()
    print('Server: ',response)


client.close()    
