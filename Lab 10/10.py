#problem 1
def power(x,n):
	if n==0:
		return 1
	else:
		return x*power(x, n-1)

# print(power(2,5))

# problem 2
def interleave(L1,L2):

	if len(L1)==0:
		return []
	# else:
	# 	L = []
	# 	L.append(L1[0])
	# 	L.append(L2[0])

	return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])
	# else:
	# 	return L1[0], L2[0]
# L=[]
# print(interleave([1,2,3,4],["a","B","c","d"]))

#problem 3
def reverse_rec(L):
	print(L)
	if len(L)==0:
		return []

	return reverse_rec(L[1:]) + [L[0]]

# L=[1,2,5,6]
# print(reverse_rec(L))

#problem 4
def zigzag(L):
	if len(L) == 0:
		print(" ")
	elif len(L) == 1:
		print(L[0], end = " ")
	else:
		
		zigzag(L[1:-1])
		print(L[0], L[-1], end = " ")

zigzag([1,2,3,4,5,6])


def is_balanced(s):
	if (s.find(")") != s.find("(")) and (s.find(")") ==-1 or s.find("(") ==  -1):
		return False
	if (s.find(")") < s.find("(")):
		return False
	elif (s.find(")") ==-1 and s.find("(") ==  -1 ):
		return True
	return(is_balanced(s.replace("(","",1).replace(")","",1)))



s="(well (I think), recursion works like that (as far as I know))"
print(is_balanced(s))
