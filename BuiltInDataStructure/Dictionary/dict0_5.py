# Creating a dictionary of lists
d = {
    'list1': [n for n in range(0, 20)],
    'list2': [n for n in range(1, 20)],
    'list3': [2*i for i in range(1, 11)]
}

print("key                              Values")
for (k, ls) in d.items():
    print(k, "-> ", ls)
    print()


# Creating a dictionary of dictionary means nested dictionary
dic = {
    'd1': {
        1: 10,
        2: 20,
        3: 30
    },

    'd2': {
        'a': 'vowel',
        'e': 'vowel',
        'i': 'vowel',
        'o': 'vowel',
        'u': 'vowel'
    },

    'list1': [n*6 for n in range(1, 11)]
}

for (key, data) in dic.items():
    print(key, '->', data)
