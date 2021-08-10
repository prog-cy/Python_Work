# Creating a tuple
# Tuple is an ordered immutable built-in data structure
"""
        1. Method 1
        t = (1, 2, 3, 4, 5, 6)

        2. Method 2
        t = tuple((2, 3, 4,4))
"""

# Creating tuple using method 1
t = (1, 2, 3, 4, 5, 6, 7)
print(t)
print(type(t))

# t[0] = 45 tuples are immutable due to that it will throw an error

# Creating tuple using method 2
t1 = tuple((10, 20, 30))
print(t1)

# Creating tuple of one element
t2 = (30, ) # Notice here t2 = (30) is not a tuple declaration
print(t2)

# Iterating tuple and getting value using index
for i in range(len(t)):
    print(t[i],  end = " ")

print()
for d in t:
    print(d, end= ' ')




