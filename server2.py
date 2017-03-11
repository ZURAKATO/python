#Server Process
#import the socket module
import socket
import sys

print("Server Starts!")

#create socket class object
s = socket.socket()

#get the host name / local machine name
host = socket.gethostbyname(socket.gethostname())
print(host)
#host = "127.0.0.1"
print("Host Name: ",host)

#reserve a post no. on which the client process will commun
port = 52345

#bind the port with the host
s.bind((host,port))

#wait for the client's request / connection
s.listen(1)     #arg - max no. of requests ?

#iterate indefinitely

for i in range(1,6):
    #accept the incomming connection
    cobj, addr = s.accept()
    print("Connection Established with Client IP: ",addr[0], " & Port: ",addr[1])
    str1 = "Thank You for connecting with %s"%(host)
    #send the string to the client
    cobj.send(str1.encode('ascii'))
    #Accepting message from the client....
    while True:
        data=cobj.recv(55334426)
        if not data:
            break
        print("------------------------------------------------------")
        print("The data Received from Clent :",data.decode('utf-8'))
        print("\n")
        print("------------------------------------------------------")
        print('Enter Data to be send to Client\n')
        data1=input()
        print("Sending to client  Data",)
        cobj.send(data1.encode('utf-8'))
    #close the connection
    cobj.close()
    print("Connection Closed with Client")
sys.exit()
