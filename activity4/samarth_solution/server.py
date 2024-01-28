import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"  
    port = 12345

    server_socket.bind((host, port))
    server_socket.listen(1)  # Allow only one connection

    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received from client: {data}")

        if data.lower() == "bye":
            print("Client requested to terminate. Closing connection.")
            break

        response = input("Enter your response: ")
        client_socket.send(response.encode('utf-8'))

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
