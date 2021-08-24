#passing n number arguments as parameter
def fun(*num):

	for n in num:
		print(n, end = " ")

fun(10, 20, 30, 40, 50)
print()

def name(*people):
	for person in people:
		print(person)

name("rupesh", "ram", "vaibhau", "Aakriti", "Anand")

#passing argument as keyword

def keyword(name = "someone",  age = 0):
	print("My name is "+str(name)+" and I am "+str(age)+" years old.")

keyword(age = 21) # passing argument as keyword.