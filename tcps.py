
# 服务器端
import socket
from time import ctime
#import time 
HOST=''

PORT=int(input('输入端口'))

BUFFERSIZE=1024 #缓冲区大小
ADDR=(HOST,PORT)




sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建ｓｏｃｋｅｔ　流式套接字
#设置服务器信息
sockfd.bind(ADDR)#bind  只能传一个参数bind（(host,port)） 绑定服务器　ip　port 


#设置监听套接字　５　是一个　队列　表示　让　队列等待
sockfd.listen(5)

#阻塞等待　接收客服端连接请求
#sockfd.accept()  #等待客户端的　连接　 
# 准备接收客户端连接
#connfd 新的套接字用来与客户端通信

connfd,addr=sockfd.accept()
print(connfd,addr)
print('connet from ',ADDR)
while 1:
	data=connfd.recv(BUFFERSIZE) #缓冲区  协调两者之间的　速率

	print('receive data:',data)
#connfd.send('ctime()',(time.ctime(),data).encode())
	connfd.send(('[%s]recv:%s'%(ctime(),data)).encode())



connfd.close()
sockfd.close()























