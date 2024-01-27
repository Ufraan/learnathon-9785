#we use the del keyword to delete items from a list or delete the list itself entirely.


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


#in this, we deleted the second item, the last item and the first two items using the del keyword.
#so the output will be as follows:
# ['Python', 'C++', 'C', 'Java', 'Rust', 'R']
# ['Python', 'C++', 'C', 'Java', 'Rust']
# ['C', 'Java', 'Rust']

#path: day_10/lists/remove_item_using_del.py