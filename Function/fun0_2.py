# problem on functions
"""
# 1 Write a program to print even numbers using function and range is passed from main function
# defining function even
def even(ran):
    for ev in range(0,ran+1, 2):
        print(ev, end=' ')

# defining main function like other languages and even function called from this function
def Main():
    n = int(input("Enter range: "))
    even(n)

# To check existance of Main function
if __name__ == '__main__':
    Main()

"""

"""
# 2. Write a program to print odd numbers using function and pass range from Main function
def odd(ran):
    for od in range(1, ran+1, 2):
        print(od, end=" ")
def Main():
    n = input("Enter range: ")
    odd(int(n))

if __name__ == '__main__':
    Main()
"""

"""
# 3. Write a program using function to find factorial of a number
def fact(num):

    f = 1
    for i in range(1, num+1):
        f*=i
    return f
def Main():
    n = int(input("Ente number: "))
    f = fact(n)
    print("Factorial of", n, 'is', f)

if __name__ == '__main__':
    Main()
"""

"""
# 4. Write a program to print all paper sizes using function
def paper_size(l, b):
    for i in range(9):
        print("A"+str(i),'=', l, 'x', b)
        t = l
        l = b
        b = t//2

paper_size(1189, 841)  # Calling function
"""

"""
# 5. Write a program to find all prime factor of a number
def PFact(n):
    i =2
    res = 1
    while n >1:
        while n%i!=0:
            i += 1
        print(i,'x', end = ' ')
        res *= i
        n = n//i
    return res

def Main():
    flag = 1
    while flag:
        num = int(input("Enter number: "))
        print("\nPrime Factor")
        res = PFact(num)
        print("\b\b=", res)
        ch = input("Enter choice (yes/No)")
        if ch!='yes':
            flag = 0

if __name__ == '__main__':
    Main()
"""
"""
# 6. Write a program  using function to find prime numbers between a given range
def Prime(ran):
    for i in range(2,ran+1):
        for j in range(2, i+1):
            if i%j == 0:
                break
        if i == j:
            print(i, end = " ")

def Main():
    flag = 1

    while flag:
        n = int(input("Enter range: "))
        Prime(n)

        ch  = input("\nEnter (y/n)")
        if ch != 'y':
            flag = 0
if __name__ == '__main__':
    Main()
"""


