#The symmetric difference between two sets A and B includes all elements of A and B without the common elements.



# this is set 1
A = {2, 3, 5}

# this is set 2
B = {1, 2, 6}


print('using ^:', A ^ B)
print('using symmetric_difference():', A.symmetric_difference(B)) 