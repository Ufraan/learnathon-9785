A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

C = A.copy()  
print(C)

print(A.union(B))  

print(A.intersection(B))  

print(A.difference(B))  

print(A.symmetric_difference(B))  