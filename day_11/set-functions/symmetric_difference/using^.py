#symmetric difference using ^ operator 

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {'i'}
print(A ^ B)
print(A ^ B ^ C)

'''OUTPUT
{'a', 'b', 'e'}
{'b', 'a', 'i', 'e'}
'''