approximation =0
while i<1001:
	approximation += ((-1)**i)/(2*i+1)
	i+=1

print(approximation*4)