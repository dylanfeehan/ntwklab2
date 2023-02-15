from socket import *
import datetime

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 12001))

clientSocket.connect(('127.0.0.1', 12000))
message = "hey"
clientSocket.send(message.encode())

response = clientSocket.recv(1024)
print(response.decode())

clientSocket.close()

print(datetime.datetime.now())
