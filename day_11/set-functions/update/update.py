#the update() method adds elements from a set (passed as an argument) to the set (calling the method).

A = {1, 3, 5}
B = {2, 4, 6}
C = {0}

print('Original A:', A)
A.update(B, C)
print('A after update()', A)

'''OUTPUT:
Original A: {1, 3, 5}
A after update() {0, 1, 2, 3, 4, 5, 6}
'''

#Here, initially set A only has 3 items. When we call update(), the items of B and C are added to set A.
