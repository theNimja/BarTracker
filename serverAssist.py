import os,socket,datetime,sys,time
ip = socket.gethostbyname(socket.gethostname())

def sendMessageToServer(productID,corporateMessage= "Access from user"):
    userName = socket.gethostname()+"@"+ip
    msg = str(8)+","+userName+","+str(productID)+","+corporateMessage
    server.sendall(bytes(msg,"UTF-8"))

while True:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip,8000))
    sendMessageToServer("foo")    server.close()
    time.sleep(60)
