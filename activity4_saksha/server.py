import socket

def main():
    host = socket.gethostname()
    port = 4000
    print("[Server] Host is:", host, "Port is:", port)

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(3)

    connection, address = server_socket.accept()
    print("[Server] Connection Details:", str(address))

    while True:
        data = connection.recv(512).decode()
        if not data:
            break
        print("[Server] Data Received from Client:", str(data))
        data = input("[Server] Enter Information to Send to Client: ")
        connection.send(data.encode())

    connection.close()

if __name__ == "__main__":
    main()
