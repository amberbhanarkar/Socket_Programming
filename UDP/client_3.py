import socket
from _thread import *
import threading
srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srv.connect((socket.gethostname(),1243))
def msgFunc1(s):
    while True:
        inpt1=input()
        inpt1=inpt1.encode()
        s.send(inpt1)
        inpt2=input()
        inpt2=inpt2.encode()
        s.send(inpt2)

def msgFunc2(s):
    while True:
        msg1=s.recv(100)
        if len(msg1)!=0:
            print("Value:", msg1.decode())

thrd1=threading.Thread(target=msgFunc1, args=(srv,))
thrd2=threading.Thread(target=msgFunc2, args=(srv,))
thrd1.start()
thrd2.start()
thrd1.join()
thrd2.join()
srv.close()