#Write a Python program to remove item(s) from a given set
my_set = {1, 2, 3, 4, 5}
items_to_remove = {3, 5}
my_set -= items_to_remove
print("Updated set after removing items:", my_set)


'''OUTPUT

Updated set after removing items: {1, 2, 4}
'''