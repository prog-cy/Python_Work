"""
working with python Operators
"""

# Arithmetic Operator
# +, -, *, /, %
print('Arithmetic Operator')
a = 3;  b= 5
print("Sum of two numbers: ", a+b)
print("Subtraction of two numbers: ", a-b)
print('Multiplication of two numbers: ', a*b)
print("Division of two numbers: ", a/b)
print("Modulus of two numbers: ", b%a)
print('\n')

# Assignment Operator
# +=, -=, *=, /=
print(" Assignment Operator")
v1 = 2; v2 = 5
v1 += v2
print("v1+=v2 = ", v1)

v1 -= v2
print('v1-=v2= ', v1)

v1 *= v2
print('v1*=v2= ', v1)

v1 /= v2
print("v1/=v2= ", v1)

v1 %= v2
print("v1%=v2= ", v1)
print('\n')

# Relational Operator
# >=, <=, ==, !=, >, <
print("Relational Operator")
v3 = 1; v4 = 1
print("Result of '==' operator: ", v3 == v4)
print("Result of '>=' operator: ", v3 >= v4)
print("Result of '<=' operator: ", v3 <= v4)
print("Result of '>' operator: ", v3 > v4)
print("Result of '<' operator: ", v3 < v4)
print("Result of '!=', operator: ", v3 != v4)
print('\n')

# Logical Operator
# and, or , not
# syntax <condition1> and <condition2>
print("Logical Operator")
print('Using logical and: ',(2 > 3) and (3 > 2))
print("Using logical or:  ", (2 > 3) or (3 > 2))
print("Using logical not: ", not(2 > 3))
print("\n")

# Bitwise Operator
# Bitwise &, Bitwise |
# Left Shift <<, Right Shift >>
# Bitwise XOR ^
print("Bitwise Operator")
print("Using Bitwise & :", 4 & 5)
"""
 4 -> 1 0 0
      & & &
 5 -> 1 0 1
     -------
      1 0 0 -> 4
"""
print("Using Bitwise |: ", 4 | 5)
"""
4 ->  1 0 0
      | | |
 5 -> 1 0 1
     -------
      1 0 1 -> 5
"""
print("Left shift <<: ", 40 << 2)  # 40*(2**2)
print("Right shift >>: ", 40 >> 3)  # 40//(2**3)
print("XOR ^: ", 3 ^ 5)
"""
 3 -> 0 1 1
      ^ ^ ^
 5 -> 1 0 1
    -------
      1 1 0 -> 6
"""

print("\n")


# Ternary operator in python

data = 10 if 10 > 0 else 0

print("data: ", data) 










