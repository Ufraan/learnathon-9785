#Write a program that calculates the factorial of a given number using a for loop.

num = int(input("enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"the factorial of {num} is =  {factorial}")