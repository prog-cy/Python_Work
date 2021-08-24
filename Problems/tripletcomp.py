a = []; b = []

result = []

a_count = 0; b_count = 0

a = input().split()
b = input().split()

for i in range(len(a)):
    if a[i] > b[i]:
        a_count = a_count+1
    if a[i] < b[i]:
        b_count = b_count+1
result.append(a_count)
result.append(b_count)

for i in result:
    print(i, end = " ")