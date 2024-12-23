# x =0
# while x<=5:

#     print(x)
#     x+=1



beginn_number = int(input("Enter Your beginnig number : " ))
ending_number = int(input("Enter Your Ending Number : "))
while beginn_number <= ending_number:
    if beginn_number == ending_number:
        print(beginn_number,end='. ')
    else:
        print(beginn_number,end=', ')
    beginn_number = beginn_number + 1

    
