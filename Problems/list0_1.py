ls = [70, 20 ,30 ,5, 6 , 10, 30]

mn = ls[0]

mx = ls[0]

sm = 0
for v in ls:
    if mn>v:
        mn = v
    if mx<v:
        mx = v
    sm+=v


print("Min: ", mn)
print("Max: ", mx)
print("Sum: ", sm)
print("Average:  %0.2f"%(sm/len(ls)))
