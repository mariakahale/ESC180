def lookup(L,num):
	for i in range(0,len(L)):
		if L[i][1]==num:
			return L[i][0]

print(lookup([["CIV", 92],
["180",98],
["103", 99],
["194", 95]], 99))