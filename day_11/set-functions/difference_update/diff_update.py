#difference update method removes all elements of another set from this set.

A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

print('A before (A - B) =', A)

A.difference_update(B)

print('A after (A - B) = ', A)


'''OUTPUT
Original Set = {'a', 'g', 'c', 'd'}
A after (A - B) =  {'a', 'd'}
'''