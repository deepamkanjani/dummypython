#!/usr/bin/python
__author__='deepam'
# this is more like an integration of everything so far
import argparse
import os
from subprocess import call

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
			os.system("ls -la")
			call(["ls","-la"])



