# Crating dictionary
d = dict()

for i in range(6):
    value = input("Enter value: ")

    d[i] = value

print(d)

print('Key value of the dictionary')
for key in d.keys():
    print(key, end = ' ')

print('\nValues of the dictionary')
for value in d.values():
    print(value, end = " ")

print('\n Key and values of the dictionary')
for (key, value) in d.items():
    print(key, '-->', value)

