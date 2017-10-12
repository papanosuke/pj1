# coding: utf-8

# スコープのテスト
gv= "初期値です。" 	#大域変数


# 関数内部で大域変数を使用する例
def scopetest1():
	global gv	#大域変数であることの宣言
	print( "scopetest1　の内部では：",gv )
	gv = "scopetest1が書き換えたものです。"	

# 大域変数と同名の局所変数を使用する例
def scopetest2():
	gv = "scopetest2の局所変数gvの値です。"	
	print( gv )

# メインルーチン
print ("【大域変数gvの値】")
print ("scopetest1　呼び出し前：",gv)
scopetest1()
print ("scopetest1　呼び出し後：",gv)
scopetest2()
print ("scopetest2　呼び出し後：",gv)
