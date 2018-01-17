#!/usr/bin/env python3

import socket 
from time import ctime

#设置服务器信息

HOST = '127.0.0.1'
PORT = 8889
BUFFERSIZE = 1024
ADDR = (HOST,PORT)

#创建socket流式套接字
sockfd = socket.socket(\
    socket.AF_INET,socket.SOCK_STREAM)
#设置超时检测时间为３秒
sockfd.settimeout(3)
"""
sockfd.setsockopt(socket.SOL_SOCKET,\
    socket.SO_REUSEADDR,1)

print(sockfd.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR))
"""
#绑定服务器IP&PORT
sockfd.bind(ADDR)

#设置监听套接字
sockfd.listen(5)

#准备接受客端连接
#connfd:新的套接字用来与客户端通信
# addr : 所连接的客户端的address
while True:
	try:
    		connfd,addr = sockfd.accept()
    		print('connect from',addr)
    		print('**************************')
    		print(connfd.getpeername())
    		print(sockfd.fileno())
    		print(sockfd.getsockname())
    		print('**************************')
    		while True:
        		data = connfd.recv(BUFFERSIZE).decode()
        		if not data:
        	 	   connfd.close()
        	 	   break
        		print("receive data:",data)
        		connfd.send(('[%s] recv:%s'%(ctime(),data)).encode())
	except:
		print('登ｌ好久')









#关闭套接字
sockfd.close()
