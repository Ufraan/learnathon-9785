#Write a program to check if a given number is prime. Use a for loop to iterate through possible divisors and break out of the loop if the number is found to be non-prime. 


num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")