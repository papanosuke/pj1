# coding: utf-8

# 加算する関数
def argtest1(*a):
	n = len(a)
	for m in range(n):
		print( a[m] )
	return n
	
# メインルーチン
a = argtest1 ("a",1,"b",2,5,6,7,8,9,10)
print ("引数の個数",a)
