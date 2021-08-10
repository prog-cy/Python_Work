"""
    working with conditional statement in python
"""

# There are three types of conditional statement in python
"""
    if
    if - else
    if - elif - else
"""

# if statement
"""
    syntax
    if (condition):
        instruction
        ---
        ---
        ---
boolean value of condition is true then inside instruction will execute otherwise not
"""

a = 20
if a == 20:
    print('a is equal to 20\n')


# if - else statement
"""
 syntax
 
 if(condition):
    instruction
    -----
    -----
 else:
    instruction
    ----
    ----
boolean value of condition is true then inside instruction of if  will execute otherwise else instruction will execute
"""
n = 50; n1 = 40
if n < n1 :
    print(n, 'is less than', n1)
else:
    print(n, 'is greater than ', n1)
print('\n')

# if-elif-else statement
"""
    syntax
    if(condition):
        instruction
        -----
        -----
    elif(condition1):
        instruction
        -----
    elif(condition2):
        instruction
        ------
    else:
        instruction
        -----
        -----
"""
n2 = 10; n3 = 10

if n2 > n3:
    print(n2, 'is greater than ', n3)
elif n2 == n3:
    print(n2, 'is equal to', n3)
else:
    print(n2, 'is less than', n3)