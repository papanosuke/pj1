# coding: utf-8

f =open("test06-1.txt","r")

while True:
	s = f.readline().rstrip()
	if s:
		print(s)
	else:
		break
f.close()
	
