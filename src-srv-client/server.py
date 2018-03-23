import sys
import socket
import pickle
import select
import sched, time
from thread import *


# Very primitive server:
# There are up to 4 clients.
# Each of them sends U/D/L/R
# Server collects these once per loop
# And sends them back a list with all instructions, i.e:
# P1 sends U
# P2 sends D
# P3/4 send nothing
# Return for all 4 of them would be: [U,S]
# As in: Player1 up and Player2 down. 
# Clients can then pass these commands manually to their Commander which should handle everything

keys = dict()
keys['Up'] = ['Up','w','i','t']
keys['Down'] = ['Down','s','k','g']
keys['Left'] = ['Left','a','j','f']
keys['Right'] = ['Right','d','l','h']
def mapKey(i,key):
	return keys[key][i]
	
host = socket.gethostname()
port = 9999
server.bind((host, port))
server.listen(2)


# Python program to implement server side of chat room.
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
host = socket.gethostname()
port = 9999 
server.bind((IP_address, Port))
server.listen(4)
 
list_of_clients = []
 
def clientthread(conn, addr):
	while True:
			try:
				message = conn.recv(32)
				if message:
					# if server got a buttonpress, broadcast it to all clients
					broadcast(message_to_send, conn)
 				else:
					"""message may have no content if the connection
					is broken, in this case we remove the connection"""
					remove(conn)
 			except:
				continue

"""Using the below function, we broadcast the message to all
clients who's object is not the same as the one sending
the message """
def broadcast(message, connection):
	# find out the ID of connection and use it for the keymapping
	for clients in list_of_clients:
		try:
			clients.send(message)
		except:
			clients.close()
			# if the link is broken, we remove the client
			remove(clients)
 
"""The following function simply removes the object
from the list that was created at the beginning of 
the program"""
def remove(connection):
	if connection in list_of_clients:
		list_of_clients.remove(connection)
 
clientIDs = dict()
i = 0
while True:
	"""Accepts a connection request and stores two parameters, 
	conn which is a socket object for that user, and addr 
	which contains the IP address of the client that just 
	connected"""
	conn, addr = server.accept()
	clientIDs[addr] = i
	i += 1
 
	"""Maintains a list of clients for ease of broadcasting
	a message to all available people in the chatroom"""
	list_of_clients.append(conn)
 
	# prints the address of the user that just connected
	print("{} connected".format(addr[0]))
 
	# creates and individual thread for every user 
	# that connects
	start_new_thread(clientthread,(conn,addr,i))	
conn.close()
server.close()