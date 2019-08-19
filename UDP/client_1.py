import socket
serverAddressPort= ("127.0.0.1", 20001)
bufferSize= 1024
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
while True:	
	msgFromClient=input("Client:")
	bytesToSend= str.encode(msgFromClient)
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	if msgFromClient=='[e]':
		break
	msgFromServer = UDPClientSocket.recvfrom(bufferSize)
	msg = "Message from Server {}".format(msgFromServer[0])
	#print(msgFromServer[0])
	if msgFromServer[0]=='[e]':
		break
	print(msg)

 
