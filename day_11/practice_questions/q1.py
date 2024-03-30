#Write a Python program to add member(s) in a set

my_set = set()
def add_members(some_set, *args):
    for item in args:
        some_set.add(item)
add_members(my_set, 1, 2, 3, 4)
print("Updated set:", my_set)


'''OUTPUT

Updated set: {1, 2, 3, 4}

'''