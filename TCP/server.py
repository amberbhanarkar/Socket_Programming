import socket
srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((socket.gethostname(), 1243))
srv.listen(5)
print("Estabilishing connection")
connection, Client = srv.accept()
print("Connection established with: ", Client)
while True:
    inpt=input("Message from Server: \n")
    if (inpt=="shutdown"):
    	connection.send(inpt.encode())
    	srv.close()
    	exit()
    connection.send(inpt.encode())
    recv_inpt = connection.recv(100)
    print("Message from Client: \n", recv_inpt.decode())
    if(recv_inpt.decode()=="Connection Closed"):
    	print("Estabilishing connection")
    	connection,Client=srv.accept()
    	print("Connection established with: ",Client)