# server.py
# Shivanshi Visvanatha, 30211537, ENSF460 Lab1

import socket

user_2 = input("Enter your name: ")

# this creates a TCP/IP socket
print("Creating TCP/IP socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # allow immediate reuse
server_address = ('localhost', 6000)
print(f"Starting up program on {server_address}")
sock.bind(server_address)

# listening for any kind of inbound connections
print("Starting to listen for connections")
sock.listen(1)

print("Waiting for a connection")
connection, client_address = sock.accept()

try:
    print(f"Connection is from {client_address}")
    name = connection.recv(1500).decode('utf-8')
    if not name:
        print("No name received")
    else:
        print(f"{name} has connected!")

    connection.sendall(bytes(user_2, 'utf-8'))
    
    while True:
        # receiving something from the client
        received = connection.recv(1500).decode('utf-8')
        if not received or received.lower() == "bye":
            if received:
                print(f"{name}: {received}")
            print(f"{name} has disconnected.")
            break
        print(f"{name}: {received}")
        
        # sending something to the client
        send = input(f"{user_2}: ")
        connection.sendall(bytes(send, 'utf-8'))
        if send.lower() == "bye":
            break
        
finally:
    print("Connection closed.")
    connection.close()
    print("Closing socket")
    sock.close()
