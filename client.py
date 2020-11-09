# Client.py
# Simple one-way chat, client recive message from server !!
# Ib Helmer Nielsen, UCN october 2020

host = "127.0.0.1"  # Set to address of server
port = 7913  # Set to port used by server

from socket import *  # Imports socket module

s = socket(AF_INET, SOCK_STREAM)  # Creates a socket
s.connect((host, port))  # Connect to server address

msg = s.recv(1024)  # Receives data upto 1024 bytes and stores in variables msg
print("Message from server : " + msg.strip().decode('ascii'))
s.close()  # Closes the socket and end the program