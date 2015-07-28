import os,socket,time,urllib.request
ip = socket.gethostbyname(socket.gethostname())


def sendMessageToServer(productID,corporateMessage= "Access from user"):
    userName = socket.gethostname()+"@"+ip
    msg = str(1)+","+userName+","+str(productID)+","+corporateMessage
    print(msg)
    server.sendall(bytes(msg,"UTF-8"))

cod= "Erk"
while (not cod.isdigit()):
    print("What  code do you with to create?")
    cod=input()

print("What is your thing?")
thingy = input()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip,8888))
sendMessageToServer(cod)
time.sleep(10)

server.sendall(bytes(thingy, "UTF-8"))
server.close()

searchPage="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=" + str(cod)
urllib.request.urlretrieve(searchPage ,os.getcwd()+"/"+"QR.png")

