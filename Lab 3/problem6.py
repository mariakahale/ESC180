#part a
def next_day(d,m,y):

	leap_year=False
	#if the year is divisible by 400
	if y%400 ==0:
		leap_year=True

	#if the year is divisible by 4
	elif y%4 == 0:
		leap_year=True

	#if the year is divisible by 100, it is NOT a leap year
	elif y%100 ==0:
		leap_year=False


	#now for the months
	#if it is a month with 31 days
	if m == 1 or 3 or 5 or 7 or 8 or 10 or 12:
		month_days = 31

	#if it is february
	elif m == 2:
		if leap_year == True:
			month_days = 29

		#if it's a regular Feb
		else:
			month_days = 28
	
	#if it's a 30-day month
	else:
		month_days = 30


	#now for the days
	#if it's not a boundary day
	if d < month_days:
		d+=1

	#if it is a boundary day
	elif d== month_days:
		d=1


		#if it is the end of the year
		if m == 12:
			d=1
			m=1
			y+=1
		#for
		else:
			m+=1


	return d,m,y

print(next_day(30,12,1599))