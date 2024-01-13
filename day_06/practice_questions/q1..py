#> Write a program that checks if a given number is positive, negative, or zero. If it's positive, print "Positive number." If it's negative, print "Negative number." If it's zero, print "Zero."

number = float(input("Enter a number: "))

if number > 0:
    print("Positive number.")
elif number < 0:
    print("Negative number.")
else:
    print("Zero.")

