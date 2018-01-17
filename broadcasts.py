from socket import *
import sys
from time import sleep
port=int(input('端口'))
# 设置广播地址　broadcast 是广播地址　别名
dest=('<broadcast>',port)

s=socket(AF_INET,SOCK_DGRAM)
#设置套接字属性为可发送接受广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)# 设置套接字　属性
print('press ctrl c to stop')

while 1:
	sleep(2)
	s.sendto('村民们　开会了'.encode(),dest)
	data,addr=s.recvfrom(1024)
	print('接受消息是',data.decode())

