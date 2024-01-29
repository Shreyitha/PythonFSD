import socket

def server():
    host = '127.0.0.1'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")
    client_socket, client_address = server_socket.accept()
    print(f"Connection  with {client_address} has been established")
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Client: {data}")
        if data == 'bye':
            print("Client requested to terminate!!")
            break
        response = input("Server: ")
        client_socket.send(response.encode('utf-8'))
        if response == 'bye':
            print("server terminated!!")
            break
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    server()
