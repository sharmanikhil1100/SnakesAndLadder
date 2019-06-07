import socket
from thread import *
import select 
import sys

#a - sent message
#b - recv message                       

 
def clientthread(conn, addr,i):
	print "Connected to :" + "<" + addr[0] + ">"
	conn.send("          Let's Play         ")  #b1
	#print conn.recv(2048)
	
	buf = conn.recv(2048)  #a1
	if buf == "Enter player1 name... ":
		buf = conn.recv(2048)  #a2
		broadcast(conn, buf)  #b2
	i = i+1
	print 'Player ' + str(i) + ' playing'
	while True:
		try:
			message = conn.recv(2048)  #a3
			if message:
				broadcast(conn, message)  #b3
			message = conn.recv(2048)  #a4
			if message:
				broadcast(conn, message)  #b4
			elif message == 'bye':
				print "connection ended with " + "<" + addr + ">"
				remove(conn)

		except:
			continue

def broadcast(conn, smessage):
	for sock in list_of_conn:
		if sock!=conn:
			try:
				sock.send(smessage)
			except:
				remove(sock)

def remove(conn):
	if conn in list_of_conn:
		conn.close()
		list_of_conn.remove(conn)
port = 12301

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', port))


s.listen(5)

list_of_conn = []
i = 0 
while True:
	conn, addr = s.accept()
	list_of_conn.append(conn)
	
	print "<" + addr[0] + ">" + "ADDED IN CHAT s"	
	start_new_thread(clientthread,(conn, addr,i))
	
s.close()	











