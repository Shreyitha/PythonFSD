import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ser_address = (socket.gethostname(), 690)

client.connect(ser_address)

while True:
    message = input("Enter your request : ")
    client.send(message.encode())

    if message.lower() == 'bye':
        print("Terminating client program.")
        break

    response = client.recv(1024).decode()
    print(f"Received response from server: {response}")

client.close()
