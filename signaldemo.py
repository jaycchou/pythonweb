from signal import *



def fun(sig,frame):
	if sig==SIGINT:
		print('收到ｃｔｒｌ＋ｃ')
	elif sig==SIGQUIT:
		print('收到ｃｔｒｌ＋\\')
signal(SIGINT,fun)
signal(SIGQUIT,fun)
#阻塞函数　，直到　某个信号　则停止阻塞
print('等待信号...')
pause()
print('进程结束')
