# Client.py
# Simple Client that send text ("Hello Server") string to server
# Ib Helmer Nielsen, UCN november 2020

host = "127.0.0.1"                  # Set to address of server
port = 7913                         # Set to port used by server

from socket import *                # Imports socket module

s = socket(AF_INET, SOCK_STREAM)    # Creates a socket
print("Connection to server...")
s.connect((host, port))             # Connect to server address
print("Send msg Hello server!!")
data = "Hello server!!"
s.send(data.encode('utf-8'))        # Encode data to utf-8 and sends data to server
msg = s.recv(1024)                  # Receives upto 1024 bytes from server and stores it in variables msg
print("Back from server : " + msg.strip().decode('ascii'))
s.close()                           # Closes the socket and end the program