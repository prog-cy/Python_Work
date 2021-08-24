# performing some operation upon dictionary using some predefined method
dic = {
    'Name': 'Rupesh',
    'Age': 21,
    'Profession': 'Programmer',
    'Hobby': 'Playing Badminton',
    'Liked Food': 'Veg biryani'
}

print("dictionary is ", dic)
for key in dic.keys():
    print(dic[key], end = " ")

print()
dic.popitem() # Removes last key and values from the dictionary
print('dictionary is ', dic)

dic.pop('Hobby') # removes values from a given key
print('dictionary is ', dic)

# Invoking values from the dict using reference
for key in dic.keys():
    print(key, ': ', dic.get(key))

print()
# Without using get(k) method
for (k, data) in dic.items():
    print(k, ':', data)

print()
print(dic.fromkeys([1, 2, 3, 4], {'a': 'Ram'}))
print()
print(dic)

print()
dict1 = dic.copy() # copying a dictionary to another
print(dict1)

dict2 = dict1 # copying a dictionary to another
print('\ndict2', dict2)

# cleaning entire dict2
dict2.clear()
print('\ndict2', dict2)

