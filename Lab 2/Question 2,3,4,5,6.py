#Question 2
memory=[100]

def my_sqrt(x):
	sqr = x**.5
	return sqr

#Question 3
def display_current_value(x):
	return memory[-1]

#Question 4
def add(to_add):
	current_value = to_add+memory[-1]
	return current_value


#Question 5
def mult(to_mult):

	current_value= to_mult*memory[-1]
	return current_value

#Question 6
def div(to_div):
	current_value = memory[-1]/to_div
	return current_value

#Question 7

def memory_function(memory, current_value):
	memory.append(current_value)

def recall(memory):
	print(memory)

#Question 8
def undo(memory):
	memory.pop()

if __name__ == "__main__":
	print("Welcome to the calculator program.\nCurrent Value:", str(display_current_value(memory)))
	print("My sqrt", my_sqrt(25))

	current_value =add(5)
	memory_function(memory,current_value)


	current_value = mult(6)
	memory_function(memory,current_value)


	current_value = div(3)
	memory_function(memory,current_value)


	recall(memory)
	undo(memory)

	print(memory)


