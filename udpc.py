from socket import *
import sys

#if len(sys.argv)<2:
#	print('argv is error')
#	sys.exit(1)


HOST=''#host= sys.argv[1]
PORT=int(input('输入端号'))# port=int(sys.argv[2])


ADDR=(HOST,PORT)
sockfd=socket(AF_INET,SOCK_DGRAM)
#sockfd=socket()
#sockfd.connect(ADDR)

while 1:
	data =input('发送消息是')
	if not data:
		break
	sockfd.sendto(data.encode(),ADDR)
	data,addr=sockfd.recvfrom(4096)
	print(data.decode())
sockfd.close()
