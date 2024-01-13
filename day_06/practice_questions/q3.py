#Write a program that determines whether a given year is a leap year or not. A leap year is either divisible by 4 but not divisible by 100, or it is divisible by 400.


year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
