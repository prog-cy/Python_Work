"""
 Control statements in python
"""

# There are mainly two control statements in python
# for loop
# while loop

# for loop
"""
 syntax
 for in range(n):
    instruction
    ---
    ---
inside ths for loop instruction will execute until the value of n becomes (n-1) and it starts with default value '0'
range(start, end, steps) is built in function in python and default starting value is '0' and end value is (end-1) and 
default step value is '1' 
"""
print("Using for loop")
for i in range(5):
    print(i,'-> Rupesh ')
print('\n')

# while loop
"""
    syntax
    
    initialize i = 0
    while(condition):
        instruction
        -----
        -----
        -----
        increment i by 1 or decrement i by 1
the loop will execute until the condition becomes false
    
"""
print("Using while loop")
i = 0
while i < 5:
    print(i, '-> Rupesh ')
    i += 1
print('\n')




