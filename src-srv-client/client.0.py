import sys
import socket as sc
import pickle

try:
	server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
except:
	print("Failed to create socket. MSG: {}".format("NO MSG"))

host = sc.gethostname()
port = 9999
server.connect((host,port))

while True:
	data = "Up"
	data = pickle.dumps(data)
	server.send(data)
	data = server.recv(1024)
	data = pickle.loads(data)
	print(data)

server.close()