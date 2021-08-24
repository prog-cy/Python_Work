# A list is a built - in data structure in python which contains dissimilar data type
# declaring a list in python
"""
    1. Method 1
    ls = [1, 2,3,4 'a', 3.45, True, False, 'rupesh']
    // Accessing element ls[0], ls[1], ls[2]

    2. Method 2
    ls = list()

    3. Method 3
    ls = input().split() #split() is predefined method which creates a list of char

"""
# Defining a list using first method
ls = [1, 2, 3, 4, 5, 6, 7, 8]
print("list ", ls)

# printing every element of the list
for i in range(len(ls)):
    print(ls[i], end = ' ')

# Defining a list using second method
print()
l = list()
print("list ", l)

n = input()
l.append(n) # append(argument) is predefined method to add element in the list at the end of the list
print('list after adding data ', l)

# Creating a list without using above defined method
l1 = input().split() # split() is predefined method which splits a string and gives output as list

print("list ", l1)

sm = 0
for d in l1:
    sm += int(d)
print("Sum of values in list l1 = ", sm)