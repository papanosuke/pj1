# coding: utf-8

# 加算する関数
def argtest2(**ka):
	print( "名前：",ka["name"] )
	print( "年齢：",ka["age"] )
	print( "国籍：",ka["country"] )
	n = len(ka)
	return n	
# メインルーチン
a = argtest2(name="tanaka",country="japan",age="41")
print ("引数の個数",a)
