import socket
import ssl
serverIP = '192.168.50.14'   
serverport = 12000
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('server.crt')

sentence = input('Input lowercase sentence: ')
try:
    clientSocket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=serverIP)
    clientSocket.connect((serverIP, serverport))
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:', modifiedSentence.decode())
except Exception as e:
    print('Error:', e)
finally:
    clientSocket.close()
