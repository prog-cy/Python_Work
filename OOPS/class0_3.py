class Student:

  college_name = "Galgotias University" #class attribute

  def __init__(self, name, age, branch):
      self.name = name
      self.age = age
      self.branch = branch
  
  #method in Student class
  def display(self):
    print('Name: ', self.name)
    print('Age: ', self.age)
    print('Branch: ', self.branch)
    print('College Name: ', self.college_name)
  
  #method with parameter
  def liveIn(self, hostel_name):
    print(self.name + " lives in "+  hostel_name)

  #method with parameter
  def goesMarket(self, market_name):
    print(self.name +" buys essential from the "+market_name)
  
#creating object of Student class
student1 = Student("Rupesh Kumar Dwivedi", 20, "Computer Science And Engineering")
student2 = Student("Radha", 21, "Civil Engineering")
student3 = Student("Ritik", 21, "Computer Science and Engineering")

print("Student first Information")
student1.display()
student1.liveIn("EZ Stays")
student1.goesMarket("Pari Chowk")

print("\nStudent second Information")
student2.display()
student2.liveIn("Galgotias Hostel")
student2.goesMarket("Delhi")

print("\nStudent third Information")
student3.display()
student3.liveIn("Einstein stays")
student3.goesMarket("Faizabad")