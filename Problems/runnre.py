n = int(input())
arr = map(int, input().split())

ls = list(arr)

# Arranging list element in descending order
for i in range(n):
    for j in range(i+1, n):
        if ls[i] < ls[j]:
            t = ls[i]
            ls[i] = ls[j]
            ls[j] = t

# Find the second max value as runner-up score
score = ls[1]
for i in range(2, n):
    if score == ls[0]:
        score = ls[i]
print(score)