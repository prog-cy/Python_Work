# list comprehension

ls = [i for i in range(10)] # creating a list using list comprehension

print(ls)

ls1 = [n for n in range(20) if n%2 == 0]
print(ls1)

ls2 = [[a, b] for a in range(10) for b in range(10) if (a+b) != 2]
print(ls2)

ls3 = [{a: b} for a in range(10) for b in range(2, 12)] # Creating a list of dictionaries
print(ls3)

matrix = [[a, b, c] for a in range(2) for b in range(a+1) for c in range(b+1)]

for row in matrix:
    for data in row:
        print(data, end = " ")
    print()
