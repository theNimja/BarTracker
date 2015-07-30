import os,socket,datetime,sys,time


HOST = ""   # Symbolic name, meaning all available interfaces
PORTNUM = 8000 # Arbitrary non-privileged port
port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    port.bind((HOST, PORTNUM))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
print ('Socket bind complete')
message = None

message=port.listen(10)
print ('Socket now listening')
os.system('serverAssist.py')
#now keep talking with the client
while True:
    for filename in os.listdir ("data/"):
        lastTime=os.path.getmtime("data/"+filename)
        if (lastTime<=time.time()-(60)):
            os.remove("data/"+filename)
            print("deleted!")
    while True:
        #wait to accept a connection
        try:
            conn, addr = port.accept()
            print ('Connected with ' + addr[0] + ':' + str(addr[1]))
            message=conn.recv(1024)
            break;
        except:
            print("")
        
    message = str(message)
    print (message)
    message= message [2:len(message)-1]
    splitted= message.split(",")
    data={}
    if (splitted[0]=="0"):
        
        data = {"productID":splitted[2],"accessFrom":splitted[1], "message":splitted[3]}
        print("Access to product "+data["productID"]+"  from "+data["accessFrom"]+", message is "+data["message"])
        if (os.path.isfile("data/"+data["productID"]+".txt") ): 
            fobj = open("data/"+data["productID"]+".txt", "a")
            stringToWrite=str(datetime.datetime.now())+" "+data["accessFrom"]+" "+data["message"].replace(" ","_")
            fobj.write(stringToWrite+"\n")
            fobj.close()
            fbin = open("data/"+data["productID"]+".txt","r")
            mulligans= fbin.readlines()
            fbin.close()
            length = len(mulligans)
            conn.sendall(bytes(str(length),"UTF-8"))
            for i in mulligans:
                print("sending "+i)
                conn.send(bytes(i,"UTF-8"))
            fbin.close()
        else:
            conn.sendall(bytes("ERROR","UTF-8"))

    if (splitted[0]=="1"):
        data = {"productID":splitted[2],"accessFrom":splitted[1], "message":splitted[3]}
        print("Creation of  product "+data["productID"]+"  from "+data["accessFrom"]+", message is "+data["message"])
        if (not os.path.isfile("data/"+data["productID"]+".txt") ):
            fobj = open("data/"+data["productID"]+".txt", "a")
            thingmajig = conn.recv(1024)
            fobj.write(str(thingmajig)[2:len(str(thingmajig))-1]+"\n")
            stringToWrite=str(datetime.datetime.now())+" "+data["accessFrom"]+" "+data["message"].replace(" ","_")
            fobj.write(stringToWrite+"\n")
            fobj.close()
        else:
            print("File exists, not valid")


   
    #out of checking on wat do
    conn.close()
    print("Closed")
