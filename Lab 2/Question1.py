def my_sqrt(x):
    sqr = x**.5
    return sqr

def my_print_square(x):
    print(x**2)
    
my_print_square(25)

#part a) there is no print/output statement. The return statement simply returns the value of 'sqr' to the main function.
#part b)the value of sqr is saved under the parameter 'res' in the main function. Therefore, 'sqr' is a local variable and does not exist in the main block.
        #you can modify it by using print(res)

#part c)calling my_print_square will print x^2 to the screen. calling my_sqrt will simply return the value stored in sqr to the calling code in the  main block.