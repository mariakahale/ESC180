def gcd(n, m):
	greatest_common_divisor = 1

	for i in range(greatest_common_divisor, max(n,m)):
		if n%i==0 and m%i== 0:
			greatest_common_divisor = i
	return greatest_common_divisor

def approach_two(n,m):
	divisor = min(n,m)
	gcd_found=False
	while gcd_found == False and n>0:
		if n%divisor==0 and m%divisor== 0:
			gcd_found = True
		else:
			n-=1

	return divisor
print(approach_two(32,16))