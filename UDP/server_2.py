import socket
from _thread import *
import threading
lck = threading.Lock()
srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((socket.gethostname(), 1243))
srv.listen(5)
def Read(s):
    while True:
        recv_input=s.recv(100)
        print("Client:",recv_input.decode())

def Send(s):
    while True:
        send_input=input()
        s.send(send_input.encode())
        if(send_input=="shutdown"):
            s.close()
            thrd2.join()
            thrd1.join()


def Start_New_Connection(connection):
    thrd1=threading.Thread(target=Read, args=(connection,))
    thrd2=threading.Thread(target=Send, args=(connection,))
    thrd1.start()
    thrd2.start()
    thrd2.join()
    thrd1.join()

while True:
    connection, Client = srv.accept()
    print("Connection Estabilished")
    Start_New_Connection(connection)

