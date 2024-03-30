#the intersection update method removes the items in this set that are not present in another, specified set.


A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}
A.intersection_update(B, C)
print('A =', A)
print('B =', B)
print('C =', C)

'''OUTPUT:

A = {4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}
'''