#add string and dictionary keys to a set using update() method

alphabet = 'odd'

number1 = {1, 3}
number2 = {2, 4}
number1.update(alphabet)

print('Set and strings:', number1)
key_value = {'key': 1, 'lock' : 2}
number2.update(key_value)

print('Set and dictionary keys:', number2)

'''OUTPUT
Set and strings: {1, 3, 'o', 'd'}
Set and dictionary keys: {'lock', 2, 4, 'key'}

Note: If dictionaries are passed to the update() method, the keys of the dictionaries are added to the set
'''