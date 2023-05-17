def list1_start_with_list2(list1,list2):
	Tracker = True
	#checks if list 1's length is greater than or equal to list 2's.
	if not len(list1)>=len(list2):
		return False

	if Tracker == True:
		for i in range(0, len(list2)):
			if list2[i] != list1[i]:
				return False
				Tracker = False

	return True


if __name__=="__main__":
	print(list1_start_with_list2([1,2,3,4,5],[1,2,3]))