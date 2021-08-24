N = int(input())

l = []
for i in range(N):
    ls = input().split() # input().split() creates a list of string and then we can convert elements according to us
    if ls[0] == "insert":
        l.insert(int(ls[1]), int(ls[2]))
    elif ls[0] == "print":
        print(l)
    elif ls[0] == "remove":
        l.remove(int(ls[1]))
    elif ls[0] == "append":
        l.append(int(ls[1]))
    elif ls[0] == "sort":
        l.sort()
    elif ls[0] == "pop":
        l.pop()
    else:
        l.reverse()
