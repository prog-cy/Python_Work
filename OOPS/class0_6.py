#In this class I will demonstrate inheritance in python

#parent class
class Shape:
  def __init__(self, len, wid):
    self.len = len
    self.wid = wid

#Child class inherits all the property of Shape class
class Rectangle(Shape):
  
  def getArea(self):
    print('Area of Rectangle: ', self.len * self.wid)
  
  def getParameter(self):
    print('Parameter of Rectangle: ', 2*(self.len + self.wid))

#Child class Inherits all the property of Shape class
class Square(Shape):

  def check(self):
    if(self.len == self.wid):
      return True
    else:
      return False
  
  def getArea(self):
    if(Square.check(self)):
      print("Area of square: ", self.len * self.wid)
  
  def getParameter(self):
    if(Square.check(self)):
      print("Parameter of square: ",  2*self.len)


#creating object of Rectangle class
shape1 = Rectangle(20, 10)
shape1.getArea()
shape1.getParameter()

#creating object of Square class
shape2 = Square(5, 5)
shape2.getArea()
shape2.getParameter()