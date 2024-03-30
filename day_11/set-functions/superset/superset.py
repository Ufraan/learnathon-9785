#the superset function returns True if set A is a superset of set B, otherwise False.

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}
print(A.issuperset(B))
print(B.issuperset(A))
print(C.issuperset(B))


'''
output

True
False
True

'''