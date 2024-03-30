#with other iterables as arguments passed to isdisjoint() method.

A = {'a', 'e', 'i', 'o', 'u'}
B = ['d', 'e', 'f']
C = {1 : 'a', 2 : 'b'}
D = {'a' : 1, 'b' : 2}
print('A and B are disjoint:', A.isdisjoint(B))
print('A and C are disjoint:', A.isdisjoint(C))
print('A and D are disjoint:', A.isdisjoint(D))

'''OUTPUT:
A and B are disjoint: False
A and C are disjoint: True
A and D are disjoint: False

'''