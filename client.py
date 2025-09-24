# client.py
# Shivanshi Visvanatha, 30211537, ENSF460 Lab1

import socket

user_1 = input("Enter your name: ")

print("Opening TCP socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 6000)
print(f"Connecting to {server_address}")
sock.connect(server_address)

try:
    print("Sending name to server")
    sock.sendall(bytes(user_1, 'utf-8'))
    
    print("Receiving server name")
    server_name = sock.recv(1500).decode('utf-8')
    if server_name:
        print(f"Connected to {server_name}!")

    while True:
        # sending something to the server
        send = input(f"{user_1}: ")
        sock.sendall(bytes(send, 'utf-8'))
        if send.lower() == "bye":
            print("Connection closed.")
            break
        
        # receiving something from the server
        received = sock.recv(1500).decode('utf-8')
        if not received or received.lower() == "bye":
            if received:
                print(f"{server_name}: {received}")
            print("Server disconnected.")
            break
        print(f"{server_name}: {received}")

finally:
    print("Closing socket")
    sock.close()
