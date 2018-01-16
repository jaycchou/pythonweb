# 多进程　

from socket import *
import os

import sys
from signal import *

import traceback


HOST=''
PORT=int(input('输入端口'))
ADDR=(HOST,PORT)

sockfd=socket()
# 默认就是　流式套接字
sockfd.bind(ADDR)
sockfd.listen(5)




while 1:
	try:
		c,addr=sockfd.accept()
	except KeyboardInterrupt:
		raise
	except :
		traceback.print_exc()
		continue 
	print('connect from',c.getpeername())

	#处理僵尸进程
	signal(SIGCHLD,SIG_IGN)
	pid=os.fork()
	print(os.fork)

	if pid<0:
		print('错误')
		continue
	elif pid>0:
		c.close()
		continue
	else:
		sockfd.close()
		while 1:
			data = c.recv(4096).decode()
			if not data :
				break 
			print(data)
			c.send('receive your message'.encode())
		c.close()
		sys.exit(0)
sockfd.close()
















