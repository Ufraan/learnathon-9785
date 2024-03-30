#using | operator to perform union of two sets

A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}

print('A U B =', A| B)
print('B U C =', B | C)
print('A U B U C =', A | B | C)


'''
OUTPUT:
A U B = {2, 'a', 'c', 'd'}
B U C = {1, 2, 3, 'c', 'd'}
A U B U C = {1, 2, 3, 'a', 'c', 'd'}
'''