def duplicates(list0):
	Tracker = False
	for i in range(0, len(list0)-1):

		if list0[i] == list0[i+1]:


			Tracker = True

	return Tracker

if __name__=="__main__":
	print(duplicates([1,2,3,3]))

