s = input()

s = s.split(" ")

new = []

for word in s:
    s1 = ''
    for i in range(len(word)):
       if i == 0:
           s1+=word[i].upper()
       else:
            s1+=word[i]
    new.append(s1)


s2 = " ".join(new)

print(s2)