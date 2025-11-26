import socket
from socket import *

serverIP = '192.168.50.132'   
serverport = 12000
sentence = input('Input lowercase sentence: ')
try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverIP, serverport))
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:', modifiedSentence.decode())
except Exception as e:
    print('Error:', e)
finally:
    clientSocket.close()
