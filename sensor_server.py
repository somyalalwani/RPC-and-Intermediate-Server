import schedule
import time
import socket

def request():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1',8050))
        x="isRequest"
        s.sendall(x.encode())
        request=s.recv(5000).decode()
        print(request)
        if request!="No Requests Yet!":
            data=""
            if request=="1":
                with open("1.txt","r") as f:
                    data=f.read()
                with open("1.txt","w") as f:
                    f.write("")
                s.sendall(data.encode())
            elif request=="2":
                with open("2.txt","r") as f:
                    data=f.read()
                with open("2.txt","w") as f:
                    f.write("")
                s.sendall(data.encode())
            

schedule.every(7).seconds.do(request)

while True:
    schedule.run_pending()