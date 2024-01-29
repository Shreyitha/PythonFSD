import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "localhost"  
    port = 12345       

    client_socket.connect((host, port))
    print(f"Connected to the server:")

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode('utf-8'))

        if message.lower() == "bye":
            break

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: ")

    print("Closing connection with the server")
    client_socket.close()

if __name__ == "__main__":
    start_client()
