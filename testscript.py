#!/usr/bin/python
__author__='deepam'
# this is more like an integration of everything so far
import argparse
import os
from subprocess import call
import socket
import re

class linux:

	def getVal(self):
		if(self.myvar == "redhat1"):
			return "New Version of Linux needs to be installed"
		elif(self.myvar == "UNIX"):
			return "unix"
		else:
			return "I am not aware"

	def __init__(self, anydistro):
		self.myvar = anydistro

parser = argparse.ArgumentParser(description="Will add this later")
#made it false for test
#parser.add_argument('-os', type=str, help="Define the operating system as either redhat1 or unix", required=False)
parser.add_argument('-os', type=str, help="Define the operating system as either redhat1 or unix", required=True)
parser.add_argument('-m', type=str, help="Add an optional parameter", required=False)

#  change it to a dictionary
cmdargs = parser.parse_args()

#  access the parameter based on the flag
osvar = cmdargs.os
#if(osvar == NULL):
#	osvar = input("Please specify the operating system")
ovar = cmdargs.m
#if(ovar == NULL):
#	ovar = input("Please specify the operating system")

newOperatingSystem = linux(osvar)
newOperatingSystem1 = linux(ovar)

for i in range(1,10):
	print(newOperatingSystem.getVal())


#while True:
#	i=1+1
#	print(newOperatingSystem1.getVal())
#	if(i == 10):
#		break

newTestData=["redhat1","UNIX"]
for i in newTestData:
	if(linux(i).getVal() == "unix"):
			print(os.getenv("PATH"))
			#os.system("ls -la")
			#call(["ls","-la"])


print(socket.gethostbyaddr("8.8.8.8"))
print(socket.gethostbyname("www.google.com"))


mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#addr=('localhost',5555)
#mysock.connect(addr)

try:
	msg="hi this is a test\n"
#	mysock.sendall(msg)
except sock.errno:
	print("Socket Error")
finally:
	mysock.close()

# try banner grabbing

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect(("www.microsoft.com", 80))

http_get = "GET / HTTP/1.1\nHost: www.microsoft.com\n\n"
data = ''
try:
	sock1.sendall(http_get)
	data=sock1.recvfrom(1024)
except:
	print("Socket error", socket.errno)
finally:
	print("Closing Connection")
	sock1.close()
strdata=data[0].decode("utf-8")
headers=strdata.splitlines()

for s in headers:
	if re.search('Server:', s):
		s = s.replace("Server: ", "")
		print(s)


