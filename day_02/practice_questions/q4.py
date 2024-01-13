# Get user input for length and width



a = int(input("Enter the value of variable 'a': "))
b = int(input("Enter the value of variable 'b': "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("\nAfter swapping:")
print("a =", a)
print("b =", b)