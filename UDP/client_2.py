import socket
from _thread import *
import threading
srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srv.connect((socket.gethostname(),1243))
def Send(s):
    while True:
        message=input()
        s.send(message.encode())
        if(message== "shutdown"):
            s.close();
            exit()
def Read(s):
    while True:
        msg1=s.recv(100)
        if len(msg1)!=0:
            print("Server:", msg1.decode())

thrd1=threading.Thread(target=Send, args=(srv,))
thrd2=threading.Thread(target=Read, args=(srv,))
thrd2.start()
thrd1.start()
thrd1.join()
thrd2.join()
srv.close()