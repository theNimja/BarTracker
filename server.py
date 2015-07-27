import os,socket,datetime,sys
HOST = ''   # Symbolic name, meaning all available interfaces
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
        #wait to accept a connection - blocking call
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
        fobj = open(data["productID"]+".txt", "w")
        
        stringToWrite=str(datetime.time.hour)+":"+str(datetime.time.minute)+":"+str(datetime.time.second)+" "+str(datetime.date.day)+"/"+str(datetime.date.month)+"/"+str(datetime.date.year)+" "+data["accessFrom"]+" "+data["message"].replace(" ","_")
        fobj.write(stringToWrite)
        fobj.close()
