from socket import *
from _thread import *

request=[]
response=[]

def sensor(a):
    global request
    global response
    ans=""
    if "1" in a:
        request.append('1')
        while len(response)==0:
            pass
        ans=response[0]
        response=response[1:]
    elif "2" in a:
        request.append('2')
        print("in sensor 2", len(request))
        while len(response)==0:
            pass
        ans=response[0]
        response=response[1:]

    return ans 


def check_request():
    global request
    global response
    if len(request)>0:
        val=str(request[0])
        request=request[1:]
        if(val=="1" or val=="2"):
            final_ans=sensor(val)
    return final_ans


def Request_List(clientsocket):
    global request
    global response

    if len(request)==0:
        clientsocket.sendall("No Requests Yet!".encode())
    else:
        x=str(request[0])
        request=request[1:]
        clientsocket.sendall(x.encode())
        ans=clientsocket.recv(5000).decode()
        response.append(ans)


def thread_con(clientsocket):
    global request
    global response
    rd = clientsocket.recv(5000).decode()
    if rd.startswith("sensorid"):
        sensorid=rd.split(":")[1]
        print("sensor id :" +sensorid)
        request.append(sensorid)
        ans=check_request()
        clientsocket.sendall(ans.encode())

    elif rd.startswith("isRequest"):
        Request_List(clientsocket)

    else:
        ans="Wrong method called! Particular Method not Present at server"
        clientsocket.sendall(ans.encode())



def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind(('127.0.0.1',8050))
    serversocket.listen(5)
    while(1):
        (clientsocket, address) = serversocket.accept()
        start_new_thread(thread_con, (clientsocket,))

    serversocket.close()
    #serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)


print('Server Started!!')
createServer()



"""
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
client_connection, client_address = server_socket.accept()
data = client_connection.recv(1024).decode('utf-8')
client_connection.send(y)
client_connection.close()
server_socket.close()
"""
