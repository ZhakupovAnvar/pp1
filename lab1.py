#PYTHON laboratory work 1
#Zhakupov Anvar

#PYTHON Syntax
#ex 1
print("Hello World")
#ex 2
if 5 > 2:
    print("YES")

#PYTHON Comments
#ex 1
#This is a comment
#ex 2
"""
This is a comment
written in 
more than just one line
"""

#PYTHON Variables
#ex 1
carname="Volvo"
#ex 2
x = 50
#ex 3
x = 5
y = 10
print(x + y)
#ex 4
x = 5
y =10
z = x + y
print(z)
#ex 5
x,y,z = "Orange","Banana","Cherry"
#ex 6
x=y=z="Orange"
#ex 7
def myfunc():
    global x
    x = "fantastic"
#PYTHON Data Types
#ex 1
x = 5
print(type(x))

int
#ex 2
x = "Hello World"
print(type(x))

str
#ex 3
x = 20.5
print(type(x))

float
#ex 4
x = ["apple", "banana", "cherry"]
print(type(x))

list
#ex 5
x = ("apple", "banana", "cherry")
print(type(x))

tuple
#ex 6
x = {"name" : "John", "age" : 36}
print(type(x))

dict
#ex 7
x = True
print(type(x))

bool
#PYTHON Numbers
#ex 1
x = 5
x = float(x)
#ex 2
x = 5.5
x = int(x)
#ex 3
x = 5
x = complex(x)
#PYTHON Strings
#ex 1
x = "Hello World"
print(len(x))
#ex 2
txt = "Hello World"
x = txt[0]
#ex 3
txt = "Hello World"
x = txt[2:5]
#ex 4
txt = " Hello World "
x = txt.strip()
#ex 5
txt = "Hello World"
txt = txt.upper()
#ex 6 
txt = "Hello World"
txt = txt.lower()
#ex 7
txt = "Hello World"
txt = txt.replace("H","J")
#ex 7
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))