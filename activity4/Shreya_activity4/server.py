import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host=socket.gethostname() 
    port=5000      

    server_socket.bind((host, port))
    server_socket.listen(5)  
    print("Server is ready to connect")

    while True:
        client_con, addr=server_socket.accept()
        print("connected to client")
        data=client_con.recv(1024).decode()
        print(f"Received from client:{data}")

        response=input("Enter your response: ")
        client_con.send(response.encode())

        if response.lower()=="bye":
            break

    client_con.close()
    server_socket.close()

if __name__ == "__main__":
    main()
