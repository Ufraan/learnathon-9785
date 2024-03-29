#Python Program to Find the Factorial of a Number

# The standard form of a quadratic equation is:
# ax^2 + bx + c = 0
# The factorial of a number is the product of all the integers from 1 to that number.
# For example, the factorial of 6 is 1*2*3*4*5*6 = 720
# The solution of this quadratic equation is given by:


#using loop

num = 7 
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of ",num,"is ",factorial)
