# Creating a dictionary
"""
    1. Method1

    d = {key: value}

    2. Method 2
    d = dict()
"""

# using method 1
d = {
    1: 'rupesh',
    2: 'ram',
    3: 'radhika',
    4: 'rohan'
}

print(d)

# Printing values taking reference of keys
print(d[1])
print(d[2])

# Adding values to the dict
d[5] = 'radhika'
print(d)

d1 = dict({1: 'ram', 'a': 5000})
print(d1)

print(d1['a'])

d2 = dict()
d2['a'] = 4000
print(d2)