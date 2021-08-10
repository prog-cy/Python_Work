"""
Recursive function is that function in which function calls itself again and again until base condition is not
found

syntax

def fun():
    if a == 0: # base condition in recursive function
        return 1
    fun() # function calling itself
"""
"""
# 1. Write a program to find sum of natural number using recursive function
def sum_n(n):
    s = 0
    if n == 1:
        return 1
    else:
        s = n + sum_n(n-1)
    return s

def Main():
    n = int(input("Enter number up-to you want to find sum: "))
    sm = sum_n(n)

    print("Sum of first", n , "natural number is ", sm)

if __name__ == '__main__':
    Main()
"""
"""
# 2. Write a program to print all natural number up-to given limit
def print_n(n):

    if n == 0:
        return
    print_n(n-1)
    print(n, end = " ")
    
ran = input("Enter range: ")
print_n(int(ran))
"""

"""
# 3. Write a program to find factorial of number using recursive function
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

n = int(input("Enter number: "))
f = fact(n)
print("Factorial of ", n, 'is', f)
"""

"""
# 4. Write a program to print fibonacci sequence using recursive function
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

n = int(input("Enter number up-to you want fibonacci sequence: "))
print("Fibonacci sequence have total ",n, "terms" )
for i in range(n+1):
    print(fib(i), end = " ")
"""
"""

# 5. Write a program to calculate the sum of the digits of a given number using recursive function
def sdigit(n):
    if n == 0:
        return 0
    return (n%10)+sdigit(n//10)

def Main():
    num = int(input("Enter number: "))
    s = sdigit(num)
    print('Sum = ', s)

if __name__ == '__main__':
    Main()
"""

"""
# 6. Write a program to obtain the prime factor of the number
def PF(n):
    i = 2
    if n == 1:
        return 1
    while n%i != 0:
        i += 1
    print(i,' x ', end = ' ')
    return i*PF(n//i)

num = int(input("Enter number: "))
print("\b\b\b = ", PF(num))
"""



