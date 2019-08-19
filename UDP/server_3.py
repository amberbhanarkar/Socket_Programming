import socket
from _thread import *
import threading
#lck = threading.Lock()
srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((socket.gethostname(), 1243))
srv.listen(5)
def mulThread(c):
    while True:
        try:
            recv_inpt1=c.recv(100)
            if not recv_inpt1:
                print("Done!")
                break
            recv_inpt1=int(recv_inpt1.decode())
            recv_inpt2 = c.recv(100)
            recv_inpt2 = int(recv_inpt2.decode())
            if recv_inpt1 and recv_inpt2:
                print("Recieved both values")
                add=recv_inpt1+recv_inpt2
                sub=recv_inpt1-recv_inpt2
                otpt1="Addition: "+str(add)
                otpt2="Subtraction: "+str(sub)
                print("Output Sent")
                c.send(otpt1.encode())
                c.send(otpt2.encode())
        except Exception as e:
            print("Connection Closed from client")
            c.close()
            break

while True:
    connection, Client = srv.accept()
    print("Connection Estabilished")
    thrd=threading.Thread(target=mulThread, args=(connection,))
    thrd.start()
