from Problem1 import *


initialize()
add(42)
if get_current_value() == 42:
	print("Test 1 passed")
else:
	print("Test 1 failed")

initialize()
subtract(42)
if get_current_value() == -42:
	print("Test 2 passed")
else:
	print("Test 2 failed")


initialize()
add(3)
multiply(5)
if get_current_value() == 15:
	print("Test 3 passed")
else:
	print("Test 3 failed")