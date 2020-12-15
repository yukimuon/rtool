# rsatool
Python implementation of RSA 

## Prerequisite  
At least you must have python3 installed on your machine

##### To generate a key pair  
go to the repository folder and run   
`python3 rsa.py -g`  
when finished it will ask you to input 1 to print key pair to screen    

##### To encrypt  
move the file under repository folder, then run     
`python3 rsa.py -e -f <file> -k <keyfile>`  

##### To edcrypt  
move the 'enc' file under repository folder, then run  
`python3 rsa.py -d -f <encryptedfile> -k <keyfile>`  

### Example  
First, we generated a key pair by  
`python3 rsa.py -g`   
now we get `16511231,505213,217057` in the file    
To encrypt go to the repository folder, open terminal then run  
`python3 rsa.py -e -f 'test.txt' -k keypair.txt`  
To decrypt the file test.txt.enc, run  
`python3 rsa.py -d -f 'test.txt.enc' -k keypair.txt.enc`  


## To be noticed  
This repo is used to test Travis CI work
[![Build Status](https://travis-ci.com/yukimuon/rtool.svg?branch=master)](https://travis-ci.com/yukimuon/rtool)

<sub>  

Copyright (c) 2019 Nagato Yuki, WTFPL

<sub>
