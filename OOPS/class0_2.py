#creating class and also declaring some method inside the class
class DemoClass:
  name = "Rupesh" #class attribute
  age = 20
  address = "Pure parson dubey"


ob1 = DemoClass()
ob2 = DemoClass()

print(ob1.name)
print(ob2.name)
ob2.name = "Radhika" #instance attribute
'''
instance attribute "this is personal property of ob2 not the property of class"
this will not affect the class name variable
'''
print(ob2.name)
print(ob1.name)

DemoClass.name = "Joy" #this will change the class name variable
print(ob1.name)
print(ob2.name)