from socket import *
from threading import *

s=socket()
HOST=''
PORT=int(input('输入端口'))
ADDR=(HOST,PORT)
s.bind(ADDR)

s.listen(5)

#线程　处理函数　用来　处理客户端请求内容
def handler(connfd):
	print('get connection from',connfd.getpeername())
	while 1:
		data=connfd.recv(4096).decode()
		if not data:
			break
		print(data)
		connfd.send('receive your message'.encode())
	connfd.close()


while 1:
	try:
		c,addr=s.accept()
	except KeyboardInterrupt:
		raise
	except Exception as e:
		print(e)
		continue
	t=Thread(target=handler,args=(c,))	
	t.setDaemon(1)
	t.start()

s.close()
