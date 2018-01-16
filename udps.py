from socket import *
from time import ctime

HOST=''
PORT=int(input('输入客户端'))
ADDR=(HOST,PORT)

sockfd=socket(AF_INET,SOCK_DGRAM) #创建 dgram　　ｕｄｐ协议　，无连接　　不可靠　－－>　网络情况差对传输实时性　要求高

sockfd.bind(ADDR)# 绑定ｉｐ

# 发送　接受
while 1:
	print('等待消息')
	data,addr=sockfd.recvfrom(1024)
	print('接受地址 ',addr)
	sockfd.sendto(str((ctime(),data)).encode(),addr)
sockfd.close()
# 关闭　套接字　
