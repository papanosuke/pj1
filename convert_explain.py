str1 = str(10) + '20'
int1 = 10 + int("20")
print("{0}".format(str1))
print("{0}".format(int1))

#1020
str2 = str1[0:4:1]
print(str2)
int2 = len(str2)
print(int2)
print(min(str2))
print(max(str2))
