#The difference between two sets A and B include elements of set A that are not present on set B.

# this is set - 1
A = {2, 3, 5}

# this is set - 2
B = {1, 2, 6}

print('Difference using &:', A - B)
print('Difference using difference():', A.difference(B)) 