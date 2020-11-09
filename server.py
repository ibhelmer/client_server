# server.py
# Simple server, that recieves message from client and send message back
# Ib Helmer Nielsen, UCN november 2020

host = "127.0.0.1"          # Set the server address to your PC's IP address
port = 7913                 # Sets port to 7913 ( > 1023)
from socket import *        # Imports socket module

s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))        # Binds the socket. Note that the input to
s.listen(1)                 # Sets socket to listening state (simple chat app, only 1 connection !!)
print("Listening for connections.. ")
q, addr = s.accept()        # Accepts incoming request from client and returns
                            # socket and address to variables q and addr
print("Client from {0}".format(addr))  # Clint address
msg = q.recv(1024)          # Receives upto 1024 bytes from client and stores it in variables msg
print("Revieved from client : "+ msg.strip().decode('ascii'))
data = "Hello Client !!"    # Data to be send is stored in variable data from user
q.send(data.encode('utf-8'))# Encode data to utf-8 and sends data to client
s.close()                   # Close socket, end of program