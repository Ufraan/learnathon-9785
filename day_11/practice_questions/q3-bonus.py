'''
You are given two sets of integers, **`set_a`** and **`set_b`**. Implement a Python program that performs the following operations and prints the results:

1. Union: Find and print the union of **`set_a`** and **`set_b`**.
2. Intersection: Find and print the intersection of **`set_a`** and **`set_b`**.
3. Difference: Find and print the elements that are present in **`set_a`** but not in **`set_b`**.
4. Symmetric Difference: Find and print the elements that are present in either of the sets, but not in both.
'''


set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
union_set = set_a.union(set_b)
print("Union:", union_set)
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)
difference_set_a = set_a.difference(set_b)
print("Difference (set_a - set_b):", difference_set_a)
difference_set_b = set_b.difference(set_a)
print("Difference (set_b - set_a):", difference_set_b)
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", symmetric_difference_set)


'''
OUTPUT:


Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
Difference (set_a - set_b): {1, 2, 3}
Difference (set_b - set_a): {8, 6, 7}
Symmetric Difference: {1, 2, 3, 6, 7, 8}
'''