m = []
n = int(input("Enter number: "))
sum1 = 0; sum2 = 0
print("Enter values in matrix")
for i in range(n):
    ls = []
    for j in range(n):
        n1 = int(input())
        ls.append(n1)
    m.append(ls)

r = 0; c = n
for i in range(n):
    for j in range(n):
        print(m[i][j], end=" ")
        if i == j:
            sum1 = sum1+m[i][j]
        if i == r and j == c-1:
            sum2 = sum2+m[i][j]
    r = r+1
    c = c-1

    print('\n')

print("Sum is both diagonal element is", sum1, sum2)
print("Difference of diagonal sum is ", abs(sum1-sum2))
