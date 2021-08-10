"""
 How to take input by user and store it in some variable
 we will use a built-in function
 input(), this always returns a string and then we can type cast using int, float
"""

name = input('Enter your name: ')
for i in range(len(name)):
    print(i, '->', name[i])

# len(argument) is built-in function which returns length of given string

num = int(input('Enter number: '))
for i in range(num):
    print(i)



