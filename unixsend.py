from socket import *
import sys
import os

address='./sockfile'
#确保在使用　sockfile前，这个文件是不存在的
try:
	os.unlink(address)
except OSError:
	if os.path.exists(address):
		raise

sockfd=socket(AF_UNIX,SOCK_STREAM)


sockfd.bind(address)
sockfd.listen(20)


while 1:
	connfd,addr=sockfd.accept()
	print(connfd,addr)
	while 1:
		data=connfd.recv(4096).decode()
		print('receive',data)
		if not data:
			break
		connfd.send('recv your message'.encode())
	connfd.close()
socket.close()