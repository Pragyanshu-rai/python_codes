import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('localhost',9188))
while True :
    data = mysocket.recv(200)
    print(data.decode())
mysocket.close()
