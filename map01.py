# coding: utf-8
# 必要なモジュールの読込み
import time # 時間計測用
from random import randrange # 乱数発生用

#########################################################
# 偶数／奇数を判定する関数の定義 #
#########################################################
def EvenOrOdd(n):
	if n % 2 == 0:
		return( "偶 " )
	else:
		return( "奇 " )

#########################################################
# 試 み(1) #
#########################################################
# 乱数リストの生成(1) ：　短いもの
lst = list( map( randrange , [100]*10 ) )

# 偶数／奇数の識別結果
lst2 = list(map(EvenOrOdd ,lst))
print("10 個の乱数の奇数／偶数の判定 ")
print(lst)
print(lst2 ,"\n")

#########################################################
# 試 み(2) #
#########################################################
# 乱数リストの生成(2) ： 　1,000,000 個
print("1,000,000 個の乱数の奇数／偶数の判定 ")
t1 = time.time()
lst = list( map( randrange , [100]*1000000 ) )
t = time.time() - t1
print(" 乱数生成に要した時間:",t,"秒 ")

# 速度検査(1) ： for による処理
lst2 = []
t1 = time.time()
for i in range (1000000):
	lst2.append( EvenOrOdd(lst[i]) )
	t = time.time() - t1
	if i % 100000 == 0:
		print(" f o r による処理 :",i,"回　ただいま",t,"秒 ")
print(" f o r による処理 :",t,"秒 ")


# 速度検査(2) ： map による処理
t1 = time.time()
lst2 = list(map( EvenOrOdd , lst )) # m a p による処理
t = time.time() - t1
print(" m a p による処理 :",t,"秒 ")

# 判定結果の確認
#print(lst2)
