#set discard using non existent element in the set 

numbers = {2, 3, 5, 4}
print('Set before discard:', numbers)
numbers.discard(10)

print('Set after discard:', numbers)

'''OUTPUT
Set before discard: {2, 3, 4, 5}
Set after discard: {2, 3, 4, 5}



so it doesnt change, and also doesnt give any error
'''