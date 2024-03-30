#the symmetric difference update method updates the set calling the method with the symmetric difference of the set and another set.

A = {'Python', 'Java', 'Go'}
B = {'Python', 'JavaScript', 'C' }
print('Original Set A:', A)

A.symmetric_difference_update(B)
print('Updated Set A:', A)

'''OUTPUT
Original Set A: {'Python', 'Java', 'Go'}
Updated Set A: {'Java', 'C', 'Go', 'JavaScript'}


Here, set A is calling the method, so the result is updated to set A. Whereas, the set B remains unchanged.
'''