# getting values from the list using iteration

ls = []

flag = True
while flag:
    num = int(input("Enter number: "))
    ls.append(num)

    ch = input("Enter y to enter more data in the list otherwise n")
    if ch != 'y':
        flag = False

print('list is ', ls)

# List element using index value
print("\nGetting values from the list using index")
for i in range(len(ls)):
    print(ls[i], end = ' ')

print("\nGetting values from the list without using index")
# list element
for x in ls:
    print(x, end = ' ')