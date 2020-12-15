import random
import secrets
import time
import os
import argparse
import hashlib

#The function to get the greatest common divisor
def gcd(a,b):
	while (a>0):
		b=b%a
		(a,b)=(b,a)
	return int(b)

#The function to get the least common mmultiple
def lcm(a,b):

	if gcd(a,b)==0:
		return int(a*b)
	else:
		return int(a*b/gcd(a,b))

#The function to get Carmichael Lambda value
def carmichael(n):
	n=int(n)
	k=2
	a=1
	alist=[]

	while not ((gcd(a,n))==1):
		a=a+1

	while ((gcd(a,n))==1) & (a<=n) :
		alist.append(a)
		a=a+1
		while not ((gcd(a,n))==1):
			a=a+1

	timer=len(alist)
	while timer>=0:
		for a in alist:
			if (a**k)%n==1:
				timer=timer-1
				if timer <0:
					break
				pass
			else:
				timer=len(alist)
				k=k+1
	return k

#The function to get all the coprimes from 1 to lambda(n), return a list
def pub_e(p,q):
	lambd=lcm((p-1),(q-1))
	start=random.randint(2,1000)
	for i in range(start,lambd):
		if gcd(i,lambd)==1:
			return i
		else:
			pass
	pub_e(p,q)


#The function to generate private key exponent
def pri_exp(e,p,q):
	lambd=lcm((p-1),(q-1))
	for t in range(1,p*q):
		if (1+lambd*t)%e==0:
			d=(1+lambd*t)/e
			d=int(d)
			return d

		
def	precheck(n,d,e):
	nordic = {str(i):ord(i) for i in ['a','b','c','d','e']}
	encdic = {k:Rsa(n,e).enc(ord(k)) for (k,v) in nordic.items()}
	if 0 in encdic.values():
		print("Error key")
		exit(1)





def testkey(n,d,e):
	print('Testing key pair')
	randomlist=[random.randint(2,100000) for i in range(5)]
	print(randomlist,end=' -> ')
	enclist=[(num**e)%n for num in randomlist]
	print(enclist)
	declist=[(num**d)%n for num in enclist]
	print(declist)
	if declist!=randomlist:
		print("Invalid key pair")
		exit()
	print("Valid key")



#Generate the random 2 prime numbers
def pregenerate():
	pair=[]
	path=str(os.getcwd()) +'/primefiles/prime.txt'
	file=open(path,'r')
	line=file.readline()
	primelist=line.split(',')

	primes=len(primelist)
	prime1=primelist[secrets.randbelow(primes)]
	prime2=primelist[secrets.randbelow(primes)]

	pair.append(prime1)		
	pair.append(prime2)

	return(pair)


#Calculate complete key pair using the pregenerate prime pair
def generate():
	pair=pregenerate()
	p=int(pair[0])
	q=int(pair[1])
	n=p*q
	e=pub_e(p,q)
	d=pri_exp(e,p,q)
	print('Generating keypair')
	print(8*'=')
	while d > 999999 :
		pair=pregenerate()
		p=int(pair[0])
		q=int(pair[1])
		n=p*q
		e=pub_e(p,q)
		d=pri_exp(e,p,q)
		print(len(str(d))*'>','              ',end='\r')
	print('Key generated                     ')
	testkey(p*q,e,d)
	return [p,q,e,d]

#The class rsa, object have methods:
#generate, generate the new object and self construct, initial instance all default are 0
#publish, print the public key pair
#showprivate, print private keypair to screen
#encrypt and decrypt which are enc and dec

class Rsa:
	def __init__(self,n=0,e=0,d=0):
		self.n=n
		self.e=e
		self._d=d
	
	def generate(self):
		keys=generate()
		p=int(keys[0])
		q=int(keys[1])
		e=int(keys[2])
		d=int(keys[3])
		self.n=p*q
		self.e=e
		self._d=d

	def publish(self):
		return self.n

	def showprivate(self):
		return self._d

	def showpublic(self):
		return self.e
	

	def enc(self,ori):
		n=self.n
		e=self.e
		enc=(ori**e)%n
		return enc

	def dec(self,enc):
		n=self.n
		d=self._d
		dec=(enc**d)%n
		return dec

def encrypt(name,n,e):
	path=os.getcwd()
	encword=''
	enclist=[]

	file=str(path)+'/'+name
	writefilename=str(path)+'/'+name+'.enc'
	writefile=open(writefilename,'w')

	print('Path to is',file)
	print('Encryption in progress')
	try:
		file=open(file,'r')
	except:
		print('Error, file not found')
		

	for line in file:
		for char in line:
			ori=ord(char)
			obj=Rsa(n,e)
			enc=obj.enc(ori)
			encword=encword+str(enc)+','
			
		enclist.append(encword) 
		encword=''
			
		enclist=str(enclist)
		writefile.write(enclist[2:-3])
		enclist=[]
		writefile.write('\n')

	writefile.close()
	print('Encryption finished')


def decrypt(name,n,d,e):
	path=os.getcwd()
	encword=''
	enclist=[]
	file=str(path)+'/'+name
	writefilename=str(path)+'/'+name[:-4]

	print('Path to is',file)
	print('Now decrypt in progress')
	known={}

	if e!=0:
		precheck(n,d,e)

	file=open(file,'r')
	for line in file:
		charlist=line.split(',')
		for encchar in charlist:
			writefile=open(writefilename,'a')
			if encchar in known:
				decstring=known[str(encchar)]
			else:
				encchar=int(encchar)
				obj=Rsa(n,0,d)
				dec=obj.dec(encchar)
				decstring=chr(dec)
				known[str(encchar)]=decstring
			if(decstring=="\n"):
				pass
			else:
				print(encchar,"->",decstring,end="          \r")
			writefile.write(decstring)
			writefile.close()

	print('Decryption finished				')

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Rsa encryption and decryption tool, never use on files other than in utf_8')
	parser.add_argument('-g', help='To generate keypair',action='store_true')
	parser.add_argument('-e', action='store_true', help='The public key e')
	parser.add_argument('-d', action='store_true', help='The private key d')
	parser.add_argument('-k', type=str, help='The relative path of the file containing keypair')
	parser.add_argument('-f', type=str, help='The relative path of the file to handle')
	args = parser.parse_args()

	if args.g:
		rsaobj=Rsa()
		rsaobj.generate()
		prikey=rsaobj.showprivate()
		pubkey=rsaobj.showpublic()
		n=rsaobj.publish()
		kfile=open("keypair.txt", "w")
		kfile.write(str(n)+","+str(pubkey)+","+str(prikey))
		kfile.close()


	elif args.e:
		if not(args.k):
			print("Provide keyfile path with -k <filename>")
		name=args.f
		f = open(args.k, "r")
		key=f.readline().split(",")
		key_n=int(key[0])
		key_e=int(key[1])
		path=os.getcwd()
		file=str(path)+'/'+name
		print('Path located:',file)
		encrypt(name,key_n,key_e)

	elif args.d:
		if not(args.k):
			print("Provide keyfile path with -k <filename>")
		name=args.f
		path=os.getcwd()
		file=str(path)+'/'+name
		name=args.f
		f = open(args.k, "r")
		key=f.readline().split(",")
		key_n=int(key[0])
		key_d=int(key[2])
		try:
			key_e=int(key[1])
		except:
			key_e=0
		decrypt(name,key_n,key_d,key_e)

	else:
		parser.print_help()


