#subset in python is a function that returns True if all elements of a set are present in another set (passed as an argument). If not, it returns False.

A = {'a', 'c', 'e'}
B = {'a', 'b', 'c', 'd', 'e'}
print('A is subset of B:', A.issubset(B))
print('B is subset of A:', B.issubset(A))

'''OUTPUT:
A is subset of B: True
B is subset of A: False

'''