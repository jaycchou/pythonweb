from socket import *
#客服端
#创建和服务器端　同样的　套接字类型

sockfd=socket()

#向　服务器端发起连接请求
 
HOST=''
PORT=int(input('输入端口'))
BUFFERSIZE=4096
ADDR=(HOST,PORT)
#创建和服务器　同样的　套接字　类型
sockfd=socket()
#向服务器发起连接请求
sockfd.connect(ADDR)

while 1:
	data=input('>>>')
	if not data:
		sockfd.close()
		break
	sockfd.send(data.encode())
	data=sockfd.recv(BUFFERSIZE)

print(data)


