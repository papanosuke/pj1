name_age = {"鈴木":20,"石川":53,"吉田":26,"遠野":30}
#無限ループ
while (True):
	key = input(">> ")
	if key in name_age:
		print(key,"さんの年齢は",name_age[key],"歳です")
	else:
		print(key,"さんという名前の人は登録されていません")
