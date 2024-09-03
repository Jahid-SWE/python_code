'''list = ['browser', 'website', 'page', 'group']
print(list[1])'''  # ['browser', 'website', 'page', 'group']

#Change valu 
'''list[3]='linkedin'
print(list)''' # ['browser', 'website', 'page', 'group']

# how to add a vaul of itemn in last using append

'''list.append('facebook')
print(list)
'''
# how to add a vaul of itemn in first using insert

'''list.insert(0, 'instagram')
print(list)
'''

# remove methods for removing items
'''list.remove('website')
print(list)'''

# pop methods for removing items by indexing
'''list.pop(3)
print(list)'''

# pop methods alson delete items only last of the values
'''
list.pop()
print(list)'''



# del keywards for deleting items only for  specific index of items
'''
del list[2]
print(list)'''


# clear keyword to remove items all items
'''
list.clear()
print(list)'''


# loop list items find all items

animals = ['cat','dog','elephant', 'tiger', 'tortoise']
# for animal in animals:
#     print(animal)


# # Print all items by referring to their index number:
# animals = ['cat','dog','elephant', 'tiger', 'tortoise']
# a = 0
# while a < len(animals):
#     print(animals[a])
#     a += 1
    
list = ['cat',
        'dot',
        'go']
list.append('polash')
print(list)

tup =('man')
print(tup)
print(type(tup))