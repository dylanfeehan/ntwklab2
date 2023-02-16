from socket import *
import time
import datetime

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 12001))
clientSocket.settimeout(1)

for i in range(10):
    
    message = "Ping " + str(i + 1) + ": " +  str(datetime.datetime.now())
    print(message)
    message = message.encode()

    proceed = True
    while(proceed):
        start = time.time()    
        clientSocket.sendto(message, ('127.0.0.1', 12000))
        try:
            response = clientSocket.recv(1024)
            end = time.time()
            rtt = end - start
            print(response.decode())
            print("Round trip time: " + str(rtt))
            print()
            proceed = False
        except:
            print("Request timed out")
            continue
        
clientSocket.close()

