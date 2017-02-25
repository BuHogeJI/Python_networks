from socket import *

myHOST = ''
myPORT = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHOST, myPORT))
sockobj.listen(5)

while True:
	connection, address = sockobj.accept()
	print('Srever connected by {}'.format(address))
	while True:
		data = connection.recv(1024)
		if not data: break
		connection.send(b'echo=> ' + data)
	connection.close()