def list_to_str(L):
	output_string="["
	for num in range(0,len(L)):
		output_string += str(L[num]) + ", "

	output_string = output_string[:-2]
	output_string+="]"

	return output_string

if __name__ == "__main__":
	print(list_to_str([1,2,3,4,5]))