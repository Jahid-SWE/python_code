# x =0
# while x<=5:

#     print(x)
#     x+=1



'''beginn_number = int(input("Enter Your beginnig number : " ))
ending_number = int(input("Enter Your Ending Number : "))

length = ending_number - beginn_number + 1
print(f"The length of the sequence is: {length}")
while beginn_number <= ending_number:
    if beginn_number == ending_number:
        print(beginn_number,end='. ')
    else:
        print(beginn_number,end=', ')
    beginn_number = beginn_number + 1'''




'''beginn_number = int(input("Enter Your beginning number: "))
ending_number = int(input("Enter Your ending number: "))

# Calculate length of the range
sequence_length = len(range(beginn_number, ending_number + 1))
print(f"The length of the range is: {sequence_length}")'''

'''beginn_number = 6
ending_number = 10

sequence_length = len(range(beginn_number, ending_number + 1))
print(sequence_length)  # Output: 6
'''

    
# using while loop and if else statements 
'''count =1
while count <= 5:
    if count == 5:
        print(count, end='.')
    else:
        print(count, end=', ')
    count += 1'''

# while loop using break 
'''count = 1
while count < 5:
    print(count)
    count += 1
    if count == 4:
        break'''


# while loop here using continue 
'''count = 1
while count < 7:
    if count%2==0 :
        count = count + 1
        continue
    print(count)
    count = count + 1'''

# 7 row triangle using while loop 
row = 7
i=1 
while i<=row:
   print('*' * i)
   i +=1

