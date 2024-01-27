#Write a recursive function to find the sum of digits of a positive integer.


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage:
number = 12345
result = sum_of_digits(number)
print(f"The sum of digits in {number} is = {result}")
