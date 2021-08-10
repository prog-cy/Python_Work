# performing some operation upon the list using predefined method to handle the list
ls = list() # Creating an empty list

print(ls)
# adding element in the list using append(argument)
ls.append(20)
ls.append(30)

print(ls)
# inserting data at particular position manually
ls[0] = 34

print(ls)

# inserting data at particular position using insert(pos, data) function
ls.insert(0, 50)
ls.insert(-1, 40)
print(ls)

# reverse list using reverse() method
ls.reverse()
print(ls)

# sorting list element using sort() method
ls.sort()
print(ls)

# find index of the data in the list using index(data, start, end)
print('Index of '+str(30)+' is ', ls.index(30, 0, len(ls)))

# counting a particular element in the given list count(data)
print(str(30)+" is in list ", end = ' ')
print(ls.count(30), 'times')

# copying a list using copy()
ls1 = ls.copy()
print('After copying ls data in ls1 ', ls1)

# deleting value from a specific index from the list using pop(index) method
val = ls1.pop(len(ls1)-1)
print("Deleting a value from the ls1 ", val)

print("ls1 after deleting a value ", ls1)

# deleting specific value  of the list using remove(value) method
ls1.remove(30)

print('ls1 after deleting 30 ', ls1)
# clearing all values from the list using clear() method
ls1.clear()

print('ls1 after clearing all data ', ls1)

# extending a ls1 using extend(list) method
ls1.extend(ls)
ls1[0] = 45
print('After extending the ls1', ls1)


