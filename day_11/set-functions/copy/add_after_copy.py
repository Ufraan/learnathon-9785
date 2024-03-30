#adding items to a set after copying

numbers = {1, 2, 3, 4}
new_numbers = numbers
print('numbers: ', numbers)
new_numbers.add(5)

print('new_numbers: ', new_numbers)

''' 
Output:
numbers:  {1, 2, 3, 4}
new_numbers:  {1, 2, 3, 4, 5}
'''