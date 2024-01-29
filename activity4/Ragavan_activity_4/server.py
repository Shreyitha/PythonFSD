import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "localhost" 
    port = 12345        

    server_socket.bind((host, port))
    server_socket.listen(5)  

    print(f"Server is now ready to accept connections from client:")

    conn, addr = server_socket.accept()
    print(f"Connected to client:")

    while True:
        data = conn.recv(1024).decode('utf-8')
        print(f"Received from client:")

        if data.lower() == "bye":
            break

        response = input("Enter your response: ")
        conn.send(response.encode('utf-8'))

    print("Closing connection with the client")
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
