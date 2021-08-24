n = int(input())

x = map(int, input().split())

t = tuple(x)

print(hash(t))