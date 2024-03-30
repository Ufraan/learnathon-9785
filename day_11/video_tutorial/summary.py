# introduction to sets in python:

# definition and characteristics of sets in python:
# a set in python is like a box where you can put things. but, it's special because it only keeps unique things.
# if you try to put the same thing twice, it won't keep the second one.
# also, you can change what's inside the box after you create it.
# sets are made by putting things inside curly braces {} and separating them with commas.

# situations suitable for utilizing sets:
# sets are handy when you want to work with a bunch of things and you only care about the unique ones.
# for example, if you have a list of items and you want to know which ones are unique,
# or if you want to combine items from different lists but keep only the unique ones.
# sets are also useful for doing math-like stuff such as combining, finding what's common,
# or what's different between sets.

# methods for creating sets in python:
# making sets in python is easy. you can:
# - use curly braces {} and list the items separated by commas, like {1, 2, 3}.
# - use the set() function and give it a list or tuple with the items inside, like set([1, 2, 3]).
# - use a comprehension, which is like a fancy way of making lists, like {x for x in range(1, 4)}.

# set operations:
# set operations are actions you can do with sets. some common ones are:
# - union (|): puts together items from two sets, making sure there are no duplicates.
# - intersection (&): finds items that are in both sets.
# - difference (-): finds items that are in the first set but not in the second.
# - symmetric difference (^): finds items that are in either set, but not in both.
# example:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2
symmetric_difference_set = set1 ^ set2

# frozen sets:
# frozen sets are like sets, but once you make them, you can't change what's inside.
# they are created using the frozenset() function.
# example:
my_set = frozenset([1, 2, 3, 4, 5])

# frozen sets are useful when you want to use sets in places where you can't change them,
# like as keys in dictionaries or inside other sets.
