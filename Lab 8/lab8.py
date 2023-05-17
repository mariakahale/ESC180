import numpy as np


# # Printing matrices using NumPy:

# # Convert a list of lists into an array:
# M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
# M = np.array(M_listoflists)
# # Now print it:
# print("hi", M)




# #Compute M*x for matrix M and vector x by using
# #dot. To do that, we need to obtain arrays
# #M and x
# M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
# x = np.array([75,10,-11])
# b = np.matmul(M,x)        

# print("bye", M)
# #[[ 1 -2  3]
# # [ 3 10  1]
# # [ 1  5  3]]

# # To obtain a list of lists from the array M, we use .tolist()
# M_listoflists = M.tolist() 

# print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

def print_matrix(M_lol):
	for i in M_lol:
		print(i)
	print("\n")

def get_lead_ind(row):
	for x in range(len(row)):
		if row[x]!=0:
			return x 
	return len(row)

def get_row_to_swap(M, start_i):
	smallest_ind = get_lead_ind(M[start_i])
	smallest_row = start_i

	for i in range(start_i+1, len(M)):
		if get_lead_ind(M[i])<smallest_ind:
			smallest_ind = get_lead_ind(M[i])
			smallest_row = i  

	return smallest_row


def add_rows_coef(r1,c1,r2,c2):
	row1 = []
	row2 = []
	output_list= []
	for i in r1:
		row1.append(i*c1)
	for i in r2:
		row2.append(i*c2)

	for index in range(len(row1)):
		output_list.append(row1[index]+row2[index])

	return output_list


def eliminate(M, row_to_sub, best_lead_ind):
	for i in range(row_to_sub+1, len(M)):
		try:
			factor = int(M[i][best_lead_ind]/M[row_to_sub][best_lead_ind])
		except:
			factor = 0
		# factor = M[i][get_lead_ind(M[row_to_sub])]
		
		for j in range(len(M[i])):
			M[i][j] -= factor*M[row_to_sub][j]

	return M

def forward_step(M):

	for i in range(len(M)):
		row_to_swap = get_row_to_swap(M, i)

		M[i], M[row_to_swap] = M[row_to_swap], M[i]
		lead_row_index = get_lead_ind(M[i])
		eliminate(M,i,lead_row_index)
	return M

def eliminate_back(M, row_to_sub, best_lead_ind):
	for i in range(row_to_sub-1, -1,-1):
		try:
			factor = int(M[i][best_lead_ind]/M[row_to_sub][best_lead_ind])
		except:
			factor = 0
		# factor = M[i][get_lead_ind(M[row_to_sub])]
		
		for j in range(len(M[i])):
			M[i][j] -= factor*M[row_to_sub][j]

	return M

def backward_step(M):
	for i in range(len(M)):
		row_to_swap = get_row_to_swap(M, i)

		M[i], M[row_to_swap] = M[row_to_swap], M[i]
		lead_row_index = get_lead_ind(M[i])
		eliminate_back(M,i,lead_row_index)
	return M

# #Test stuff for get_row_to_swap
M = [[5, 6, 7, 8],
[0, 0, 0, 1],
[0, 0, 5, 2],
[0, 1, 0, 0]]
start_i = 1
print(get_row_to_swap(M, start_i))


#Test stuff for add_rows_coef
# r1=[5,6,7,8]
# c1=2
# r2=[1,0,1,0]
# c2=-1
# print(add_rows_coef(r1,c1,r2,c2))


# Test stuff for eliminate
# M = [[5, 6, 7, 8],
# [0,0, 1, 1],
# [0, 0, 5, 2],
# [0, 0, 7, 0]]
# row_to_sub = 1
# best_lead_ind = 2
# print(eliminate(M,row_to_sub, best_lead_ind))


# Test stuff for forward_step
# M=[[ 0, 0, 1, 0, 2],
# [ 1, 0, 2, 3, 4],
# [ 3, 0, 4, 2, 1],
# [ 1, 0, 1, 1, 2]]
# print_matrix(forward_step(M))


# #Test stuff for backward_step
# # M = [[ 1, -2, 3, 22],
# # [ 3, 10, 1, 314],
# # [ 1, 5, 3, 92]]
# print_matrix(backward_step(M))