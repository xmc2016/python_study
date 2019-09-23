import socket,time,threading

import argparse

socket.setdefaulttimeout(3) #设置默认超时时间

def socket_port(ip,port):



#输入IP和端口号，扫描判断端口是否占用

	

	try:

		if port >=65535:

			print(u'端口扫描结束')

		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

		result = s.connect_ex((ip,port))

		if result == 0:

			lock.acquire()

			print(ip,":",port,'端口已占用')

			lock.release()

	except:

		print(u'端口扫描异常')



def ip_scan(ip):

#输入IP，扫描IP的0-65534端口情况



	try:

		print(u'开始扫描%s' %ip)

		start_time = time.time()

		for i in range(0,65534):

			t = threading.Thread(target=socket_port,args=(ip,int(i)))

			t.start()

			t.join()				

		print(u'扫描端口结束，共用时：%.2f'%(time.time()-start_time))

          	

	except:

		print(u'扫描IP出错')



if __name__ == '__main__':

	url = input('input IP:')

	lock = threading.Lock()

	ip_scan(url)


		
