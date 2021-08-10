ls = [70, 20 ,30 ,5, 6 , 10, 30]

n = int(input("Enter element that you want search in the given list: "))

if n in ls:
    print(n, "is present at position", ls.index(n))
else:
    print(n, "is not present in the list")
