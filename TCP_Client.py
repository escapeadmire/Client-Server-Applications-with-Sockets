#add try except block for error handling



import socket
from socket import *    
serverIP = '10.8.0.6'   
serverport = 12000
sentence = input('Input lowercase sentence: ')
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverport))
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
