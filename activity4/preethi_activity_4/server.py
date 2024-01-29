import socket
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 6000
    server_socket.bind((host,port))
    server_socket.listen()
    print(f"server listening on {host} : {port}")

    
    client_socket, address = server_socket.accept()
    print(f"connected by {address}")
    
    while True:
        data = client_socket.recv(1024).decode()
        if data.lower() == 'bye':
            print("Client requested termination")
            break
        print("Data recieved", data)
        response = input("Enter you response :")
        client_socket.send(response.encode())
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()



