#we can also use remove() method to remove an item from a list.
#the remove() method removes the specified item and does not return any value.

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the second item
del languages[1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the last item
del languages[-1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust']

# delete the first two items
del languages[0 : 2]  # ['C', 'Java', 'Rust']
print(languages)


#here, we deleted the second item, the last item and the first two items using the del keyword.

#so output will be as follows:
# ['Python', 'C++', 'C', 'Java', 'Rust', 'R']
# ['Python', 'C++', 'C', 'Java', 'Rust']
# ['C', 'Java', 'Rust']

#path: day_10/lists/remove_item_using_remove.py