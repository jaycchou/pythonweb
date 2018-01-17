from greenlet import greenlet


def test1():
	print('11111111')
	gr2.switch()
	print(2222)
	gr2.switch()


def test2():
	print(333333)
	gr1.switch()
	print(4444444)
#将函数注册为　greenlet　协程
gr1=greenlet(test1)
gr2=greenlet(tset2)

#启动协程函数
gr1.switch()

