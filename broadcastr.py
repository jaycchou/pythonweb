from socket import *


host=''
port=int(input('端口'))
s=socket(AF_INET,SOCK_DGRAM)


s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.bind((host,port))
while 1:
	try:
		message,addr=s.recvfrom(2048)
		print('接受消息',message.decode())
		s.sendto('Im coming'.encode(),addr)
	except Exception as e:
		print(e)
