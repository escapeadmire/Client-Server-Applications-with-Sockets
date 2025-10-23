import socket
from socket import *

#add try except block for error handling

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    try:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()
        print("Received from client:", message.decode())
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    except Exception as e:
        print(f"Error occurred: {e}")


