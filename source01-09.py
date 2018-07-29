even = 0
odd = 0

while (True):
	a = int(input("> "))
	if a < 0:
		print("入力をやり直してください")
		continue           #処理を最初に戻す
	elif a == 0:
		print("終了します")
		print("--report------------------------------")
		print("偶数は{}個でした".format(even))
		print("奇数は{}個でした".format(odd))
		break
#
	if a % 2 == 0:
		even = even + 1
		print("{0}個目の偶数です".format(even))
	else:
		odd = odd + 1
		print("{0}個目の奇数です".format(odd))
 
