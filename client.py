from socket import *


HOST = '0.0.0.0'  
PORT = 7000        # The port used by the rpc

with socket (AF_INET, SOCK_STREAM) as mysocket:
	mysocket.connect((HOST, PORT))
	#y=str(function_calls).encode()
	
	while True:
		x=input("Enter 1 or 2:")
		if x=="1":	
			mysocket.send(x.encode())
			ans=mysocket.recv(1024).decode()
			print("Output:",end=" ")
			print(ans)
		
		elif x=="2":
			mysocket.send(x.encode())
			ans=mysocket.recv(1024).decode()
			print("Output:",end=" ")
			print(ans)
		elif x=="quit":
			print("Session ended!")
			break
		else :
			print("Wrong choice!! Try again!!")

mysocket.close()