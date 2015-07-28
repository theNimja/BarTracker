import os,socket,datetime,sys



HOST = ""   # Symbolic name, meaning all available interfaces
PORTNUM = 8888 # Arbitrary non-privileged port
port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    port.bind((HOST, PORTNUM))#
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
print ('Socket bind complete')
message = None

message=port.listen(10)
print ('Socket now listening')
 
#now keep talking with the client
while True:
    while True:
        #wait to accept a connection
        conn, addr = port.accept()
        print ('Connected with ' + addr[0] + ':' + str(addr[1]))
        message=conn.recv(1024)
        break;
    message = str(message)
    message= message [2:len(message)-1]
    splitted= message.split(",")
    data={}
    if (splitted[0]=="0"):
        data = {"productID":splitted[2],"accessFrom":splitted[1], "message":splitted[3]}
        print("Access to product "+data["productID"]+"  from "+data["accessFrom"]+", message is "+data["message"])
        fobj = open("data/"+data["productID"]+".txt", "a")
        stringToWrite=str(datetime.datetime.now())+" "+data["accessFrom"]+" "+data["message"].replace(" ","_")
        fobj.write(stringToWrite+"\n")
        fobj.close()
        fbin = open("data/"+data["productID"]+".txt","r")
        mulligans= fbin.readlines()
        fbin.close()
        print(str(mulligans))
        print(str(len(mulligans)))
        length = len(mulligans)
        conn.sendall(bytes(str(length),"UTF-8"))
        for i in mulligans:
            print("sending "+i)
            conn.send(bytes(i,"UTF-8"))
        fbin.close()
        
    conn.close()
