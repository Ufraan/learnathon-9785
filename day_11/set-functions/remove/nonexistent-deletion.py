#deleting an element which does not exist in the set will raise an error because the remove() method will raise an error if the element to be removed is not present in the set.

animal = {'cat', 'dog', 'rabbit', 'guinea pig'}
animal.remove('fish')
print('Updated animal set:', animal)


'''OUTPUT
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
    animal.remove('fish')
KeyError: 'fish'
'''


#note: You can use the set discard() method if you do not want this error.