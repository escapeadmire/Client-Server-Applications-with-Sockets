import socket
import ssl
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

print('The server is ready to receive')
while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        print(f"Connection established with {addr}")
        tls_server_socket = context.wrap_socket(connectionSocket, server_side=True)
        message = tls_server_socket.recv(1024)    
        modifiedMessage = message.decode().upper()
        print("Received from client:", message.decode())
        tls_server_socket.send(modifiedMessage.encode())
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        tls_server_socket.close()
        connectionSocket.close()
