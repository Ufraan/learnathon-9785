#the union function is used to return a set that contains all items from both sets, duplicates are not included

A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}

print('A U B =', A.union(B))
print('B U C =', B.union(C))
print('A U B U C =', A.union(B, C))

print('A.union() =', A.union())

'''
OUTPUT:
A U B = {2, 'a', 'd', 'c'}
B U C = {1, 2, 3, 'd', 'c'}
A U B U C = {1, 2, 3, 'a', 'd', 'c'}
A.union() = {'a', 'd', 'c'}
'''