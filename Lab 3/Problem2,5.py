import math
approximation =0
prediction_met = False

n=4
i=0 

new_pi=math.pi
true_rounded_pi=round(new_pi,n-1)


while i<10001 and prediction_met == False:

	approximation += ((-1)**i)/(2*i+1)

	if round(approximation*4,n-1) == true_rounded_pi:
		print("Number of sums:", str(i))
		prediction_met = True
	else:
		i+=1


# approx=0
# i=0
# while i<1001:
# 	approx += ((-1)**i)/(2*i+1)
# 	i+=1
# print(approx*4)