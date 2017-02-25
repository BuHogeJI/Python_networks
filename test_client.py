import socket

sockobj = socket.socket()
sockobj.connect(('localhost', 1488))
done = False
while not done:
	mess = input('Print a message you need to change: ')
	if mess == '': done = True
	sockobj.send(mess.encode())
	data = sockobj.recv(1024)
	print(mess, '-->', data.decode())
sockobj.close()