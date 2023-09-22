list = [9 ,1,8,2,3,7,8]
list.sort()
print(list)

items = ['alpen','man', 'face', 'apple', 'mango', 'xampp']
items.sort()
print(items)



# Reverse the order of the list items:
#items = ['alpen','man', 'face', 'apple', 'mango', 'xampp']
items = [9 ,1,8,2,3,7,8]
#items.sort()
items.reverse()
print(items)


# Make a copy of a list with the copy() method:

items = ['alpen','man', 'face', 'apple','mango', 'xampp']
items_name = items.copy()
print(items_name)

# Another way to make a copy is to use the built-in method list().
items =['alpen','man']
items_name = list(items)
print(items_name)
