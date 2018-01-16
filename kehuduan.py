from socket import *
#import socket

#sockfd=socket.socket()
sockfd =socket()
HOST=''
PORT=int(input('输入端口：'))
ADDR=(HOST,PORT)
k=4096

sockfd.connect(ADDR) #连接　ｉｐ　和端口
d=(sockfd.recv(4096)).decode()# 接受　1 list 2get
print(d)#显示　
while 1:
	data=input('>>>')
	if not data:
		sockfd.close()
		break
		while data=='2'or  data=='3' or data=='4':
			if data=='2':
				sockfd.send(data.encode())
			a=input('输入下载文件名')
			sockfd.send(a.encode())
			d=sockfd.recv(4096).decode()#接受bb文件
			print(d)
			b=input('输出下载文件名')
			f=open(b,'w')
			for i in d:
				f.write(i)
		
				f.close()
			print('复制成功')
			break

			if data=='3':
				pass
			if data=='4':
				pass
		else:
			break
	sockfd.send(data.encode())
	data=sockfd.recv(4096).decode()
	print(data)





