import socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost',9188))
serverSocket.listen(4)
(clientSocket, address) = serverSocket.accept()
data = "hello briooo"
clientSocket.send(data.encode())
serverSocket.close()
