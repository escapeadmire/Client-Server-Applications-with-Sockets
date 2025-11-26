#add try except block for error handling


from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024)
        modifiedMessage = message.decode().upper()
        print("Received from client:", message.decode())
        connectionSocket.send(modifiedMessage.encode())
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        connectionSocket.close()
