'''
    Simple socket server using threads
''' 
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 7777 # Arbitrary non-privileged port
ad=[]
i=0 
a=[] 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(5)
print 'Socket now listening'
p=[]
l=0
m=0
def clientthread(conn):
    #Sending message to connected client
    k=0
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
    for k in range(i-1):
        conn.sendall('connected with  '+ a[k]) 
        conn.sendall('\n')
    for l in range(i-1):
        ad[l].sendall('new connected client  '+str(new))    
    while True:
       #yhan c mera apna h :p

       data = conn.recv(1024)
       p.append(conn)
       print data
       p[0].sendall('you can now chat with '+ data)
       for m in range(i):
          if data == a[m]:
               p.append(a[m])
               conn = p[1]
               conn.sendall('m')
            
       
    conn.close()   
new=0     
n=0
b=[]
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr= s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    a.append(str(addr[1]))
    #p.append(addr[1])
    new= addr[1]
    #start_new_thread(connectthread ,(conn,))
    start_new_thread(clientthread ,(conn,))
    ad.append(conn)
    b.append(conn)
    i+=1
s.close()
