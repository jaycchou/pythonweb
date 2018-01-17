from socket import *
from time import ctime
#多路复用模块
from select import *

s=socket()
host=''
port=int(input('输入端口'))
addr=(host,port)
s.bind(addr)
s.listen(5)
#设置关注
inputs=[s]
outputs=[]
while 1:
	rs,ws,es=select(inputs,[],[])
	# 设置遍历返回的就绪ｉｏ事件
	for r in rs:
	# 对事件进行判断　然后处理
		if r is s:
		#接收
			connfd,addrr=r.accept()
			print('接受来自',addrr)
			print('ｃｏｎｎｆｄ是',connfd)
			#将客户端链接套接字　加入到关注列表中
			inputs.append(connfd)
		else:
			data=r.recv(1024).decode()
			print('消息',data)
			if not data:
				inputs.remove(r)
			outputs.append(r)
			
	for w in ws:
		w.send(ctime().encode())
		outputs.remove(w)
		
			
			

s.close()

















