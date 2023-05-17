def lists_are_the_same(list1, list2):
	if len(list1) != len(list2):
		return False
		
	for i in range(0, len(list1)):
		if list1[i] != list2[i]:
			return False
	return True
if __name__=="__main__":
	print(lists_are_the_same([1,2,3], [1,2,3]))
