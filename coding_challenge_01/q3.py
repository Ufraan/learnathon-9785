# Solve the quadratic equation ax**2 + bx + c = 0
import cmath

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

d = (b**2) - (4*a*c)

sol1 = (-b - cmath.sqrt(d)) / (2*a)
sol2 = (-b + cmath.sqrt(d)) / (2*a)

print('The solutions are {0} and {1}'.format(sol1, sol2))
