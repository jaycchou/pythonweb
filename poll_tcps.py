from socket import *

from select import *

s=socket()
host=''
port=int(input('输入端口'))
s.bind((host,port)) 
s.listen(5)
#创建ｐｏｌｌ对象

fdmap={s.fileno():s}

p=poll()

#注册关注事件
p.register(s)


while 1:
	#等待任意一个　注册事件就绪返回
	#[(fileno,io obj),(),()]
	events=p.poll()
	for fd,event in events:
		if fd == s.fileno():
			c,addr=s.accept()
			print('链接来自',addr)
			p.register(c)
			fdmap[c.fileno()]=c
		elif  event & POLLIN:
			data = fdmap[fd].recv(1024).decode()
			if not data:
				p.unregister(fd)
				del fdmap[fd]
			else:
				print(data)
				fdmap[fd].send('receive your message'.encode())
s.close()














