'''
Written by - Anamay Dubey
Written on - 29/01/24
Title - Problem Statement 4 Solution
'''
import socket

def server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind to the port to specific IP and port no
        server_socket.bind(('localhost', 999))

        # Listen for incoming connections, connection no is 3
        server_socket.listen(3)
        print("Waiting for incoming connections...")

        while True:
            # Establish connection with client
            client_socket, addr = server_socket.accept()
            print('Connected to client:', addr)

            try:
                while True:
                    # Receive data from client
                    data = client_socket.recv(1024).decode('utf-8')
                    print('Client:', data)

                    if data.lower() == 'bye': # if message is 'bye' loop will break
                        break

                    # Send response to client
                    response = input('Server: ')
                    client_socket.send(response.encode('utf-8'))

                # Close the client socket
                client_socket.close()
                print('Connection with client closed')
            
            except KeyboardInterrupt as ki: #CTR+C will interrupt and raise error
                print(f"{ki}Server stopped by user.")
                break

    finally:
        # Close the server socket
        server_socket.close()
        print('Server socket closed')

if __name__ == '__main__':
    server()
