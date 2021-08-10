# Creating a dictionary
d = {}

while True:
    key = input("Enter key: ")
    data = input("Enter data: ")

    d[key] = data

    ch = input("Enter y/n ")
    if ch != 'y':
        break

print(d)

for (k, data) in d.items():
    print(k, '-->', data)
    print(d.get(k))

d.popitem() # deleting value from dictionary
print(d)