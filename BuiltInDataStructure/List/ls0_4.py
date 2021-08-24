# Creating a list of string and then calculating sum of the list elements

ls = input("Enter number: ").split(' ') # using this we can create a list taking input in one

print('list is ', ls)
sm = 0
for x in ls:
    sm += int(x)
print('Sum of above list is= ', sm)

# creating and initializing values to the list
ls1 = list([2, 3, 4, 5, 5])
print(ls1)