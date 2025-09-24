# TCP Socket Chat Application
A simple real-time chat application built with Python using TCP sockets that enables two users to communicate over a network connection.

## Overview
This project implements a basic client-server chat system using Python's socket programming. It demonstrates fundamental networking concepts including TCP/IP communication, client-server architecture, and real-time bidirectional messaging.

## Features
Real-time Communication: Instant messaging between client and server
Bidirectional Chat: Both users can send and receive messages
Graceful Disconnection: Clean connection termination with "bye" command
Connection Status: Real-time connection and disconnection notifications
Error Handling: Robust handling of network interruptions and connection failures
User-friendly Interface: Simple command-line interface with clear prompts

## Prerequisites
Python 3.6 or higher
Basic understanding of command-line operations
Network connectivity (localhost for testing)

# Installation
Clone or download the project files:
bash   git clone <repository-url>
   cd tcp-chat-application
Ensure both server.py and client.py are in the same directory
No additional dependencies required - uses Python standard library only

# Usage
Starting the Server

Open a terminal/command prompt
Navigate to the project directory
Run the server:

bash   python server.py

Enter your name when prompted
The server will start listening on localhost:6000

# Connecting the Client

Open a second terminal/command prompt
Navigate to the project directory
Run the client:

bash   python client.py

Enter your name when prompted
The client will automatically connect to the server

# Chatting

Type your messages and press Enter to send
Messages will appear with the sender's name
Type "bye" (case-insensitive) to disconnect and close the application
Either user can initiate disconnection

Example Session
Server Terminal:
Enter your name: Alice
Creating TCP/IP socket
Starting up program on ('localhost', 6000)
Starting to listen for connections
Waiting for a connection
Connection is from ('127.0.0.1', 54321)
Bob has connected!
Bob: Hello Alice!
Alice: Hi Bob! How are you?
Client Terminal:
Enter your name: Bob
Opening TCP socket
Connecting to ('localhost', 6000)
Sending name to server
Receiving server name
Connected to Alice!
Bob: Hello Alice!
Alice: Hi Bob! How are you?
🔧 Technical Details
Architecture

Protocol: TCP/IP for reliable message delivery
Port: 6000 (localhost)
Buffer Size: 1500 bytes
Encoding: UTF-8

# Key Components
Server (server.py)

Creates and binds TCP socket to localhost:6000
Listens for incoming connections
Accepts one client connection at a time
Handles bidirectional message exchange
Manages connection lifecycle

Client (client.py)

Establishes connection to server
Initiates name exchange protocol
Handles user input and message transmission
Processes incoming messages from server

# Network Flow

Server starts and binds to port 6000
Client connects to server
Name exchange occurs
Bidirectional chat session begins
Either party can terminate with "bye"
Graceful connection closure

# Project Structure
tcp-chat-application/
│
├── server.py          # Server-side application
├── client.py          # Client-side application
└── README.md          # This file

Fork the repository
Create feature branches
Submit pull requests for improvements
Report issues or bugs
