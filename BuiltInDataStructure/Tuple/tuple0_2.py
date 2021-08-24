# Updating a tuple
"""
    We know that tuples are immutable we can not modify tuple directly.
    But there is an alternate method to modify the tuple.
    First we will convert it into list and we wll make modification in the list
    and then again we will convert that list into tuple
"""

t = (10, 20, 30, 40, 50, 60)
print('Before modification tuple is')
print(t)

# We have to insert data at the 2th position
ls = list(t)
ls[1] = 12
t = tuple(ls)

print("After modification tuple is")
print(t)
