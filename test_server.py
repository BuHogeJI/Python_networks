import socket


sockobj = socket.socket()
sockobj.bind(('', 1488))
sockobj.listen(1)

while True:

	connection, addres = sockobj.accept()
	print('Connected by {}'.format(addres))

	while True:
		data = connection.recv(1024)
		if data.decode() == '': data = b'empty string'
		print('I get: {}'.format(data.decode()))
		if not data: break
		connection.send(data.upper())
	connection.close()