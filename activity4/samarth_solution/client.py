import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1" 
    port = 12345

    client_socket.connect((host, port))
    print("Connected to the server.")

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode('utf-8'))

        if message.lower() == "bye":
            print("Terminating client.")
            break

        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
