# coding: utf-8
from pathlib import Path
import os

print (os.getcwd())
#p = Path(os.getcwd() + "/test06-1.txt")
p = Path("test06-1.txt")
f = p.open("r",encoding="utf-8")

while True:
	s = f.readline().rstrip()
	if s:
		print(s)
	else:
		break
f.close()

