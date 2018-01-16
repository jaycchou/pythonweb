import  socket 
from time import ctime
import os

HOST=''
PORT=int(input('输入端口：'))

#BUFFERSIZE=1024

ADDR=(HOST,PORT)


sockfd= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(sockfd)

sockfd.bind(ADDR) #绑定　ｉｐ　和　端口

sockfd.listen(55)
#q=os.getcwd()
l=os.listdir()

while 1:
	
	connfd,addr=sockfd.accept()
	connfd.send((""""
		1 list  显示所有服务器端的名字
		2 get	下载服务器端的某个文件
		3 put	上传客户端的某个文件
		4 quit	退出
		""").encode())

	print('连接来自',ADDR)

	while 1:
		data=connfd.recv(4096).decode()
		print('接收数据是',data)
		while '1'<=data<='4':
			if data=='1':
			#connfd.send(q.encode())
				connfd.send(str(l).encode())
				break
			elif data=='2':

				c=connfd.recv(4096).decode()
                                #print(c)
				aa=open(c,'r')
				bb=aa.readlines()
				connfd.send(str(bb).encode())
				break
				
			elif data=='3':
				pass
			elif data=='4':
				break
				
			elif not data:
				break
			connfd.send(ctime().encode())
		else:
			break
			
print('输入有误　直接退出')
connfd.close()
sockfd.close()
















