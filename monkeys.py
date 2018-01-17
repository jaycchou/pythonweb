
from gevent import monkey
monkey.patch_all()
import gevent
from socket import *
from time import ctime 
def acc(addr):
	while 1:
		
		connfd,addrr=s.accept()
		gevent.spawn(send,connfd,addrr)
		print('connect from',addr)
		print('addrr',addrr)
		
def send(connfd,addrr):
	try:
		while 1:
			data=connfd.recv(4096).decode()
			if not data:
				break
			print(data)
			connfd.send((ctime().encode()))
	except OSError as e:
		print(e)
	finally:
		connfd.close()

if __name__=='__main__':
	s=socket()
	host=''
	port=int(input('输入端口'))
	addr=(host,port)
	s.bind(addr)
	s.listen(5)
	acc(addr)
