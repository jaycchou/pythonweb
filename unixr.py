from socket import *
import sys
#创建　本地套接字　用　ａｆ——ｕｎｉｘ
sockfd=socket(AF_UNIX,SOCK_STREAM)

# 本地套接字不再使用　网络地址，而是用　socket类型文件
address='./sockfile'


try:
	sockfd.connect(address)
except error as e:
	print(e)


try:
	message='this is a unix message'
	sockfd.send(message.encode())
	data=socket.recv(4096).decode()
	print('recv',data)
except error as e:
	print(e)
finally:
	sockfd.close()
