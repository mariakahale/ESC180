def get_nums(L):
	new_L=[]
	for i in range(0,len(L)):
		new_L.append(L[i][1])
	return new_L
print(get_nums([["CIV", 92],
["180",98],
["103", 99],
["194", 95]]))