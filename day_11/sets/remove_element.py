#removing an element from a set

languages = {'C', 'Javascript', 'Python'}
print('Initial Set:',languages)

removedValue = languages.discard('Javascript')
print('Set after remove():', languages)