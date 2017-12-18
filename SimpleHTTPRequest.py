#!/usr/bin/python
__author__ = 'deepam'

import http.client
import argparse
import re

parser = argparse.ArgumentParser(description="Will add this later")
parser.add_argument('-d', type=str, help="Specify the domain name exactly", required=True)

#  change it to a dictionary
cmdargs = parser.parse_args()

domain = cmdargs.d
print(domain)

h = http.client.HTTPConnection(domain)
h.request("GET", "/")
data = h.getresponse()
if(data.code>200 and data.code <400):
	for s in data.headers:
		if re.search('Server:', s):
			print(data.headers)
			s = s.replace("Server: ", "")
			print(s)
text = data.readlines()

#debug to print the entire response
#for t in text:
#	print(t.decode('utf-8'))
