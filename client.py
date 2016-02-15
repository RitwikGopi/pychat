import sys
import select
import socket
port = 2005
ip = '127.0.0.1'
name = raw_input("Please enter your name: ")
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sock.bind(('',2010))
input = [sock,sys.stdin]
sock.sendto(name,(ip,port))
while True:
         inputready,outputready,exceptready = select.select(input,[],[])
         for s in inputready:
             if s == sock:
                 data,addr = sock.recvfrom(1024)
                 print data
      #       n = addr[1] 
             
             elif s == sys.stdin:
                 msg = raw_input()
                 sock.sendto(msg,(ip,port))
