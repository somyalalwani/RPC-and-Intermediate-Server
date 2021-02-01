from socket import *
import pickle
from _thread import *
#code with client to get function calls

ans=0
def thread_conn(sensor_id):
	global ans
	HOST='127.0.0.1'
	PORT=8050
	with socket (AF_INET, SOCK_STREAM) as clientsocket:
		clientsocket.connect((HOST, PORT))
		
	#clientsocket.sendall(sensor_id.encode())
		clientsocket.sendall(("sensorid :"+ sensor_id).encode())
		ans=clientsocket.recv(1024).decode()
	return

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 7000 #client_stub


server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
client_connection, client_address = server_socket.accept()

while True:
	sensor_id = client_connection.recv(4096).decode() # 1 or 2
	if(sensor_id=="1" or sensor_id=="2"):
		start_new_thread(thread_conn, (sensor_id,))
		client_connection.send(str(ans).encode())
	else:
		client_connection.send(str("Wrong choice").encode())

client_connection.close()	
server_socket.close()