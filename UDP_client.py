#add try except block for error handling


import socket
from socket import *
serverName = '192.168.50.132'
serverPort = 12000
try:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = input('Input lowercase sentence:')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
except Exception as e:
    print('Error:', e)
