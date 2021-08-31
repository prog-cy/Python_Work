import math
class Calculator:

  def __init__(self, number):
    self.number = number
  
  def square(self):
    return self.number * self.number
  
  def cube(self):
    return self.number * self.number * self.number

  def square_root(self):
    return math.sqrt(self.number)
  
cal = Calculator(25)
print("Square of ", cal.number , ' is ', cal.square())
print("Square root of ", cal.number, ' is ', cal.square_root())