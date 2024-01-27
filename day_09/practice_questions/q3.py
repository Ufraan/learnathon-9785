#How would you write a recursive function to calculate the power of a number (e.g., x^n)?

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

result = power(2, 3)
print(result)

#in this example, 2 is the base and 3 is the exponent. 2^3 = 2 * 2 * 2 = 8