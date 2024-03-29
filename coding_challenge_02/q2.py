#Python Program to Find the Factorial of a Number

# The standard form of a quadratic equation is:
# ax^2 + bx + c = 0
# The factorial of a number is the product of all the integers from 1 to that number.
# For example, the factorial of 6 is 1*2*3*4*5*6 = 720
# The solution of this quadratic equation is given by:


#using recursion
#made it simpler than the given answer
def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)

num = 7
result = factorial(num)
print("The factorial of", num, "is", result)
