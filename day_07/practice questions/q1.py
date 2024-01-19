#Write a program that takes a number as input from the user and prints its multiplication table up to 10.


num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
