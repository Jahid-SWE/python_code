'''listone = ['a','b', 'c','d' ]
listtwo =[1,2,3,4]
all_list = listone + listtwo
print(all_list)'''


listone = ['a','b','c','d']
listtwo =[1,2,3,4]
for i in listtwo:
    listone.append(i)
print(listone)