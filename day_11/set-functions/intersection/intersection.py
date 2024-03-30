#the intersection() method returns a new set with elements that are common to both sets.

A = {2, 3, 5, 4}
B = {2, 5, 100}
C = {2, 3, 8, 9, 10}
print(B.intersection(A))
print(B.intersection(C))
print(A.intersection(C))
print(C.intersection(A, B))

'''
OUTPUT:

{2, 5}
{2}
{2, 3}
{2}

'''