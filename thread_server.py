from socket import *
from _thread import *
import sys, os, time

myHost = ''
myPort = 1488

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

def handleConnection(connection):
	time.sleep(5)
	while True:
		data = connection.recv(1024)
		if not data: break
		connection.send(data.upper())
	connection.close()

def dispatcher():
	while True:
		connection, address = sockobj.accept()
		print('Connected with {}'.format(address))
		start_new_thread(handleConnection, (connection, ))

dispatcher()