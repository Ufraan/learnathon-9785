A = {'a', 'b', 'c'}
B = {'a', 'b', 'c'}
result = A.symmetric_difference(B)
print(result)

'''OUTPUT
set()
'''

#this is because both sets A and B are equal. So, the symmetric difference of two equal sets is an empty set.