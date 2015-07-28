import os,socket,time
ip = socket.gethostbyname(socket.gethostname())
#killReadOrCreate , 0= read, 1= kill,2= create
# can go to 2147483647




def sendMessageToServer(productID,killReadOrCreate=0, corporateMessage= "Access from user"):
    userName = socket.gethostname()+"@"+ip
    msg = str(killReadOrCreate)+","+userName+","+str(productID)+","+corporateMessage
    print(msg)
    server.sendall(bytes(msg,"UTF-8"))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip,8888))
sendMessageToServer("123",0)


numLines= server.recv(1024)
numLines=int(numLines)
print(str(numLines))

buffer=[]
for i in range(numlines):
    reply= server.recv(1024)
    buffer.append(string(reply,"UTF-8"))
print(buffer)
input()
