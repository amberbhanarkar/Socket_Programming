import socket
localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
y=0
# Bind to address and ip
while y==0:
# Create a datagram socket
	print("UDP server up and listening")
	# Listen for incoming datagrams
	while(True):
		bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
		message = bytesAddressPair[0]
		address = bytesAddressPair[1]
		clientMsg = "Message from Client:{}".format(message)
		clientIP  = "Client IP Address:{}".format(address)
		if message=='[e]':
			break
		print(clientMsg)
		print(clientIP)
		# Sending a reply to client
		msgFromServer=input("Server:")
		bytesToSend= str.encode(msgFromServer) 
		UDPServerSocket.sendto(bytesToSend, address)
		if msgFromServer =='[e]':
			y=1
			break

		
