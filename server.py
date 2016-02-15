#!/usr/bin/python
import socket
import sys
import select
port = 2005
ip = ''
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))
input = [sock,sys.stdin]
address = {}
while True:
    inputready,outputready,exceptready = select.select(input,[],[])
    for s in inputready:
         if s == sock:
             data,addr = sock.recvfrom(1024)
             if not addr[0] in address:
			address[addr[0]] = (data,addr[1])
			print data+" ADDED TO CHAT"
			for ipadrs in address:
                 		sock.sendto(data+" ADDED TO CHAT",(ipadrs,address[ipadrs][1]))
	     else:
			print address[addr[0]][0] + '>>' + data
			for ipadrs in address:
				if addr[0] != ipadrs:
	                 		sock.sendto(address[addr[0]][0]+'>>'+data,(ipadrs,address[ipadrs][1]))
         elif s == sys.stdin:
             msg = raw_input()
	     for ipadrs in address:
                 	sock.sendto("ADMIN>>\t"+msg,(ipadrs,address[ipadrs][1]))
	 print addr

               
