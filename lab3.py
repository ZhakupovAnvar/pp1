#PYTHON laboratory work 1
#Zhakupov Anvar

#PYTHON Functions
#ex 1
def my_function():
  print("Hello from a function")
#ex 2
def my_function():
  print("Hello from a function")

my_function()
#ex 3
def my_function(fname, lname):
  print(fname)
#ex 4
def my_function(x):
  return x + 5
#ex 5
def my_function(*kids):
  print("The youngest child is " + kids[2])
#ex 6
def my_function(**kid):
  print("His last name is " + kid["lname"])

#PYTHON lambda
#ex 1
x = lambda a : a

#PYTHON Classes
#ex 1
class MyClass:
   x = 5
#ex 2
class MyClass:
  x = 5

p1 = MyClass()
#ex 3
class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)
#ex 4
class Person:
  def __init__ (self, name, age):
    self.name = name
    self.age = age

#PYTHON inheritance
#ex 1
class Student(Person):
#ex 2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()
