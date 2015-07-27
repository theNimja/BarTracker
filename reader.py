import os,socket,time
ip = socket.gethostbyname(socket.gethostname())
#killReadOrCreate , 0= read, 1= kill,2= create
# can go to 2147483647
def sendMessageToServer(productID,killReadOrCreate=0, corporateMessage= "Access from user"):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip,8888))
    userName = socket.gethostname()+"@"+ip
    
    msg = str(killReadOrCreate)+","+userName+","+str(productID)+","+corporateMessage
    print(msg)
    server.sendall(bytes(msg,"UTF-8"))

sendMessageToServer("123",0)
