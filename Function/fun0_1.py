"""
 Functions in python

 There are mainly two types of function in python
 1. Built -in /(predefined) Function
 2. User define Function

 1. Examples of built-in function
                print(), input(), len(argument), range(argument), random(range) etc..
 2. Examples of user define function
                fun_name(arg1, arg2, arg3, ...., argn), display(), animal()

    syntax for user define function
    for that we use keyword 'def' before defining a function
    def fun_name(ar1, ar2, ar3, ......, arn):
            instructions
            ------
            ------
            ------
            ------
            ------
    fun_name(arg1, arg2,arg3, ........, angn) # calling a function

"""
# Defining a function  without parameters in python
def display():
     print("I am learning  function in python")

display() # calling function

# Defining a function with parameter
def get_value(n):
    print("Value is: ", n)

get_value(30) # passing argument  at the time of calling the function

# Defining a function which will return a value
def give_data(n):
    return n

res = give_data(50)
print('Value return by function is: ', res)

# At the time of defining a function set default values to the parameters
def set_default_value(a = 0, b = 0, c = 0):
    return a+b+c

sum1 = set_default_value()
print("Sum of three values: ", sum1)
sum2 = set_default_value(10, 30, 40)
print("Sum of three values: ", sum2)
sum3 = set_default_value(a = 10, b = 20)
print("sum of three values: ", sum3)


