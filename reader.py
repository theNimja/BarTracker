import os,socket
ip = socket.gethostbyname(socket.gethostname())
#killReadOrCreate , 0= read, 2= kill,1= create
# can go to 2147483647 usingf 32 bits




def sendMessageToServer(productID,corporateMessage= "Access from user"):
    userName = socket.gethostname()+"@"+ip
    msg = str(0)+","+userName+","+str(productID)+","+corporateMessage
    print(msg)
    server.sendall(bytes(msg,"UTF-8"))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("https://warm-depths-1688.herokuapp.com",8000))
cod = "wefg"
while (not cod.isdigit()):
    print("What code do we access")
    cod= input()

sendMessageToServer(str(cod))


numLines= server.recv(1024)
if (str(numLines)=="b'ERROR'"):
    print("This item does not exist.Please try again.")
else:
    numLines=int(numLines)

    buffer=[]
    for i in range(numLines):
        reply= server.recv(1024)
        buffer.append(str(reply,"UTF-8"))
    server.close()

     
    thing = buffer[0]
    buffer.pop(0)
    print ("This product:"+str(thing))#Later say item code
    buffer= list(reversed(buffer))
    for i in range (len(buffer)) :
        setData= buffer[i].split(" ")
        print(str(i+1)+":Access from  "+str(setData[2])+" on "+str(setData[1])+" at "+str(setData[0])+"("+str(setData[3]).replace("_"," ")+")")


input()
