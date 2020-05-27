import multiprocessing

def gck1(a,b):
	while (a>0):
		b=b%a
		(a,b)=(b,a)
	result=(int(b)==1)
	return result

def checkgck(x):
	p1 = multiprocessing.Process(target=job1,args=(x, )) 
	p2 = multiprocessing.Process(target=job2,args=(x, )) 
	p3 = multiprocessing.Process(target=job3,args=(x, )) 
	p4 = multiprocessing.Process(target=job4,args=(x, )) 
	p1.start()
	p2.start()
	p3.start()
	p4.start()
	p1.join() 
	p2.join() 
	p3.join() 
	p4.join() 
	return 'checkpass'

def job1(x):
	for t in range(1,x,5):
		if not gck1(t,x):
			print('COMPOSITE FOUND!')


def job2(x):
	for t in range(2,x,5):
		if not gck1(t,x):
			print('COMPOSITE FOUND!')


def job3(x):
	for t in range(3,x,5):
		if not gck1(t,x):
			print('COMPOSITE FOUND!')


def job4(x):
	for t in range(4,x,5):
		if not gck1(t,x):
			print('COMPOSITE FOUND!')


if __name__=='__main__':
	file=open('primefiles/prime.txt')
	line=file.read()
	num_list=line.split(',')
	timer=1
	t=len(num_list)
	for x in num_list:
		x=int(x)
		print('Testing',timer,'out of',t,end='\r')
		if x==2 or x==3 or x==5:
			x=7

		if x%5==0:
			print('COMPOSITE FOUND!')
			exit()

		if checkgck(x)!='checkpass':
			print('Error!')
			exit()
		if timer%1000==0:
			print(timer,'tested                      ')
		timer=timer+1
		if(timer==t+1):
			print("All pass                          ")
			break


