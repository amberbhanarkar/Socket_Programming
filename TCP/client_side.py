import socket
srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srv.connect((socket.gethostname(),1243))
print("Connection is estabilished between client and server")
while True:
    recv_inpt = srv.recv(100)
    print("Server:", recv_inpt.decode())
    inpt=input("Client:")
    inpt=inpt.encode()
    srv.send(inpt)