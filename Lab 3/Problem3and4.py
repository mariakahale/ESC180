def gcd(n, m):
	greatest_common_divisor = 1

	for i in range(greatest_common_divisor, min(n,m)+1):
		if n%i==0 and m%i== 0:
			greatest_common_divisor = i
	return greatest_common_divisor

def approach_two(n,m):
	divisor = min(n,m)
	gcd_found=False
	while gcd_found == False:
		if n%divisor==0 and m%divisor== 0:
			gcd_found = True
		else:
			divisor-=1

	return divisor

def simply_fraction(n,m):
	divisor = gcd(n,m)
	a_new= n/divisor
	b_new = m/divisor
	print("new fraction", str(int(a_new)), "/", str(int(b_new)))

simply_fraction(16,32)