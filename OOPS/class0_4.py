#creating Rectangle class and then claculating the area and parameter of diff-2 class
class Rectangle:

  def __init__(self, length, width):
    self.width = width
    self.length = length
  
  #method to calculate area of rectangle
  def getArea(self):
    print('Area of rectangle: ', self.length * self.width)
  
  #method to calculate parameter of rectangle
  def getParameter(self):
    print('Parameter of rectangle: ', 2*(self.length + self.width))

#creating object of Rectangle class
rectangle1 = Rectangle(20, 10)
rectangle2 = Rectangle(5, 4)

rectangle1.getArea()
rectangle1.getParameter()

rectangle2.getArea()
rectangle2.getParameter()

  