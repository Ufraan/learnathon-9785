numbers = [1, 3, 5]

even_numbers = [4, 6, 8]

# add elements of even_numbers to the numbers list
numbers.extend(even_numbers)

print("List after append:", numbers) 


#extend method adds the elements of one list to another list. so in this example, the elements of even_numbers list are added to the numbers list

#output will be as follows:
# List after append: [1, 3, 5, 4, 6, 8]
# Path: day_10/lists/append.py