ls = [70, 20 ,30 ,5, 6 , 10, 30]

for i in range(len(ls)):

    mn = i
    for j in range(i+1, len(ls)):
        if ls[mn] > ls[j]:
            mn = j

    if i != mn:
        t = ls[mn]
        ls[mn] = ls[i]
        ls[i] = t

print("Sorted list: ")
print(ls)