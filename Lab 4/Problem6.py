def match_pattern(list1,list2): 
	Tracker = True
	#iterates through all of list 1
	for j in range(len(list1)):
		#if the first item in list 2 exists in list1...
		if list1[j] == list2[0]:
			
			counter = 0	
			#iterate from that item in list 1 all the way to the number of items in list 2
			for k in range(j, len(list2)+j):
				try:
					if list1[k] != list2[counter]:
						Tracker = False
					else:
						counter +=1
				except:
					Tracker = False	
		else:
			pass

	return Tracker

if __name__=="__main__":
	print(match_pattern([1,2,3,4], [2,3]))
