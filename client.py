from socket import *
import datetime

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 12001))
clientSocket.settimeout(3)

clientSocket.connect(('127.0.0.1', 12000))

for i in range(10):
    
    message = "Ping " + str(i + 1) + ": " +  str(datetime.datetime.now())
    message = message.encode()

    proceed = True
    while(proceed):
        clientSocket.send(message)
        try:
            response = clientSocket.recv(1024)
            print(response.decode())
            print()
            proceed = False
        except:
            continue
        
clientSocket.close()

