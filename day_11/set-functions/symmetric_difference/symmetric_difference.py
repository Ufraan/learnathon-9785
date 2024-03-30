#the symmetric difference of two sets is the set of elements that are in either of the sets but not in both.

A = {'Python', 'Java', 'Go'}
B = {'Python', 'JavaScript', 'C' }
result = A.symmetric_difference(B)
print(result)

'''RESULT
{'Go', 'Java', 'C', 'JavaScript'}
'''


#Here, 'Python' is present in both sets A and B. So, the method returns all the items of A and B to result except 'Python'.