"""
# 1. Write a program to print all even numbers in given range in single line

num = int(input('Enter number up-to you want even number: '))
print("Even number between 0 to", num)
for i in range(0, num+1, 2):
    print(i, ' ', end = '')
print('\nDone\n')
"""

"""
# 2. Write a program to print all odd numbers in given range in single line

num1 = int(input('Enter number up-to you want odd number: '))
print('Odd number between 1 to', num1)
for i in range(1, num+1, 2):
    print(i, ' ', end = '')
print('\nDone\n')
"""

"""
# 3. Write a program to check that given number is positive or negative

flag = True
while ( flag ):
    n1 = int(input('Enter number which you want to check: '))
    if n1 > 0:
        print(n1, 'is Positive')
    elif n1 == 0:
        print(n1, 'is neither positive nor negative')
    else:
        print(n1, 'is negative')
    ch = input("Enter y/n : ")
    if ch != 'y':
        flag = False
print('Done\n')
"""

"""
# 4. Write a program to reverse a number

flag = True
while( flag ):
    n2 = int(input('Enter a number which you want to reverse: '))
    rev = 0
    num = n2
    while (n2 > 0):
        rem = n2 % 10
        rev = rev * 10 + rem
        n2 = n2 // 10
    print('Reverse order of ', num, 'is', rev)
    ch = input("Enter y/n: ")
    if ch != 'y':
        flag = False
print("Done\n")
"""

"""
# 5. Write a program to calculate sum of the digits of a given number

flag = True
while(flag):
    n4 = int(input('Enter number: '))
    sum1 = 0
    num = n4
    while(n4 > 0):
        rem = n4 % 10
        sum1 = sum1 + rem
        n4 = n4 // 10
    print('Sum of digits of ', num, 'is', sum1)
    ch = input("Enter y/n: ")
    if ch != 'y':
        flag = False
print('Done\n')
"""
"""
# 6. Write a program to calculate sum of first and last digit of a number
flag = True

while(flag):
    n1 = int(input('Enter number: '))
    num = n1
    while(n1>0):
        rem = n1 % 10
        n1 = n1 // 10
    first_digit = rem
    last_digit = num % 10
    last_first_digit_sum  = first_digit + last_digit
    print('Sum of first and last digit of ', num, 'is', last_first_digit_sum)

    ch = input("Enter y/n: ")
    if ch != 'y':
        flag = False
print('Done\n')
"""

"""
# 7. Write a program to check that a given number is palindrome or not
flag = True

while(flag):
    n1 = int(input("Enter number: "))
    num = n1
    rev = 0
    while(n1>0):
        rem = n1 % 10
        rev = rev*10 + rem
        n1 = n1 //10
    if (num == rev):
        print(num, 'is a palindrome number')
    else:
        print(num, 'is not a palindrome number')
    ch = input('Enter y/n: ')
    if ch != 'y':
        flag = False
print('Done\n')
"""

"""
# 8. Write a program to check a given number is prime or not
flag = True

while flag:
    n1 = int(input('Enter number: '))
    for i in range(2, n1+1):
        if n1 % i == 0:
                break
    if n1 == i:
        print(n1, 'is prime')
    else:
        print(n1, 'is not prime')
    ch = input('Enter y/n: ')
    if ch != 'y':
        flag = False
print('Done \n')
"""

"""
# 9. Write a program to check number is prime or not in given range

n = int(input('Enter up-to which number you want prime number: '))
print('Prime numbers between 2 to', n)
for num in range(2, n+1):
    for i in range (2, num+1):
        if num%i == 0:
            break
    if num == i:
        print(num, end = ' ')
print('\nDone\n')
"""

"""
# 10. Write a program to calculate the factorial of a number

flag = True
while(flag):
    n = int(input("Enter number for that factorial you want: "))
    fact = 1
    i = 1
    if n > 0:
        while (i <= n):
            fact *= i
            i += 1
        print('factorial of', n, 'is', fact)
    else:
        print(n, ' is negative ')

    ch = input('Enter y/n: ')
    if ch != 'y':
        flag = False
print('Done\n')
"""

"""
# 11. Write a program to calculate sum of first natural number

flag = True
while(flag):
    n = int(input('Enter number: '))
    sumn = n*(n+1)//2
    print('Sum of first',n, 'natural number is: ', sumn)
    ch = input("Enter y/n: ")
    if ch != 'y':
        flag = False
print("Done \n")
"""

"""
# 12. Write a program to calculate sum of all even integers in given range

n = int(input("Enter number up-to you want add all even numbers: "))
sum1 = 0

for i in range(0, n+1, 2):
    sum1 += i

print("Sum of all even numbers up-to ", n,  'is: ', sum1)
"""

"""
# 13. Write a program to print table of number entered by user

flag = True
while(flag):
    n = int(input("Enter number which table you want to print: "))
    print('Table of', n)
    for i in range(1, 11):
        print(n, 'x', i, ' = ', n*i)

    ch = input('Enter y to print new table else n to exit: ')
    if ch != 'y':
        flag = False
print("\nDone\n")
"""


