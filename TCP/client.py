import socket
srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srv.connect((socket.gethostname(),1243))
print("Connection is established between client and server")
while True:
    recv_inpt = srv.recv(100)
    print("Server:", recv_inpt.decode())
    if(recv_inpt.decode()=="shutdown"):
        print("Connection Closed")
        srv.close()
        exit()
    inpt=input("Client:")
    if (inpt=="shutdown"):
    	print("Connection Closed")
    	srv.send("Connection Closed".encode())
    	srv.close()
    	exit()
    inpt=inpt.encode()
    srv.send(inpt)