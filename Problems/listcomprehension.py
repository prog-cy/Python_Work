x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
n = int(input("n = "))

result = []
for i in range(x+1):
    for j in range(y+1):
        ls = []
        for k in range(z+1):
            if i+j+k!=n:
                ls = [i, j, k]
                result.append(ls)


print(result)

