#client process
#import the socket module
import socket

print("Client Starts!")

try:
    #create socket class object
    s = socket.socket()

    #set host and port no.
    host = input().strip()
    #host = "127.0.0.1"
    port = 52345

    #connect to the server
    s.connect((host,port))
    print("Connection Established with Server")

    #receive the string
    str1 = s.recv(1024)

    #decode the string
    print(str1.decode('ascii'))

    ##Sending a messgae To server......
    print("----------------------------------------------")
    print("Enter the meassge to be sent")
    message=input()
    while message!='-1':
        s.send(message.encode('utf-8'))
        print("Message sent!!!!!!")
        print("------------------")
        data=s.recv(55334426)
        print("------------------------------")
        print("Recived is :-",(data).decode('utf-8'))
        print("----------------------------------------------")
        print("Enter the meassge to be sent")
        message=input()

    #close the connection
    s.close()

    print("Connection Closed with Server")
except socket.error:
    print("Unable to Locate Server!")
