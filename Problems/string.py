s1 = input()
s2 = input()

t = tuple()

for i in range(len(s1)):
    j = 1
    if s1[i:len(s2)+i] == s2:
       print(s1[i:len(s2)+i])
       if i==0:
            t = (i, len(s2)-1)
       else:
           t = (i, len(s2)+i-j)
       print(t)
    j+=1


