lst = ["a","b","c","d"]

try:
	n = lst.index("c")
	print (n,"番目にあります")
except ValueError:
	print ("要素が見つかりません")
	
