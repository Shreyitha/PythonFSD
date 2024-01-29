import socket

def main():
    host = socket.gethostname()
    port = 4000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("Enter a Message to Send to Server: ")

    while True:
        client_socket.send(message.encode())
        data = client_socket.recv(512).decode()

        print("Message Received from Server:", str(data))
        message = input("Enter a Message to Send to Server: ")

        if message == "quit":
            break
        
    client_socket.close()
        
if __name__ == "__main__":
    main()
