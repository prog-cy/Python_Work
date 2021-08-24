"""
program to check duplicasy in given list of string
"""

list1 = list()
list2 = list()

#Taking input from the user and add it to the list1
for i in range(20):
    str1 = input("Enter string: ")
    list1.append(str1)

#Removing common sequence from each string in list1
for word in list1:
    str2 = ''
    for letter in word:
        if letter in str2:
            continue
        else:
            str2 = str2+letter
    list2.append(str2)

print(list1)
print('\n\n\n')
print(list2)
