def count_evens(L):
	even_counter=0
	for num in L:
		if num%2==0:
			even_counter+=1
	return even_counter

if __name__=="__main__":
	print(count_evens([1,2,3,4,5]))