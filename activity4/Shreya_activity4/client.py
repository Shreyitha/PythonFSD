import socket

def main():
    client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    host=socket.gethostname()
    port=5000 

    client_socket.connect((host, port))
    print("connected to server")

    while True:
        message=input("Enter your message: ")
        client_socket.send(message.encode())

        if message.lower()=="bye":
            break

        data=client_socket.recv(1024).decode()
        print(f"Received from server:{data} ")

    client_socket.close()

if __name__ == "__main__":
    main()