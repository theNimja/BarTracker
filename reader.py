import os,socket
ip = socket.gethostbyname(socket.gethostname())
#killReadOrCreate , 0= read, 1= kill,2= create
# can go to 2147483647 usingf 32 bits




def sendMessageToServer(productID,corporateMessage= "Access from user"):
    userName = socket.gethostname()+"@"+ip
    msg = str(0)+","+userName+","+str(productID)+","+corporateMessage
    print(msg)
    server.sendall(bytes(msg,"UTF-8"))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip,8888))
sendMessageToServer("123")


numLines= server.recv(1024)
print(str(numLines))
if (str(numLines)=="b'ERROR'"):
    print("This item does not exist.Please try again.")
else:
    numLines=int(numLines)

    buffer=[]
    for i in range(numLines):
        reply= server.recv(1024)
        buffer.append(str(reply,"UTF-8"))
    server.close()

    buffer= list(reversed(buffer))
    for i in range (len(buffer)) :
        if (i==len(buffer)-1):
            thing = buffer
            print ("This product:"+str(thing))#Later say item code
        else:
            print(buffer)
            setData= buffer[i].split(" ")
            print(str(setData))
            print(str(i+1)+"Access from  "+str(setData[2])+" on "+str(setData[1])+" at "+str(setData[0])+"("+str(setData[3]).replace("_"," ")+")")


input()
