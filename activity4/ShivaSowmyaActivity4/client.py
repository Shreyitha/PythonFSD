import socket

def client():
    host = '127.0.0.1'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Client: ")
        client_socket.send(message.encode('utf-8'))
        if message == 'bye':
            print("client got terminated!!")
            break
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {response}")
        if response == 'bye':
            print("server terminated!!")
            break
    client_socket.close()

if __name__ == "__main__":
    client()
