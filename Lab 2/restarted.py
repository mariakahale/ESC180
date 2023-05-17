previous = 0
current = 0
tempmemory = 0

def my_sqrt(x):
	sqr = x**.5
	return sqr

def display_current_value():
	print("current:",current, "previous:",previous)

#Question 4
def add(to_add):
	global previous
	global current
	previous = current
	current = to_add + previous


def mult(to_mult):
	global previous
	global current
	previous = current
	current = to_mult * previous

def div(to_div):
	global previous
	global current
	previous = current
	current =  previous / to_div

def undo():
	global previous
	global current
	temp = current
	current = previous
	previous = temp

def recall():
	global current
	global previous
	global tempmemory

	previous = current
	current = tempmemory


def memory():
	global tempmemory
	global previous
	global current

	tempmemory = current
	previous = current

if __name__ == "__main__":
	add(3)
	display_current_value()
	memory()
	display_current_value()

	div(3)
	display_current_value()


	undo()
	display_current_value()
	undo()
	display_current_value()

	recall()
	display_current_value()



	mult(5)
	display_current_value()