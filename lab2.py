#PYTHON laboratory work 2
#Zhakupov Anvar

#PYTHON While Loops
#ex 1
i = 1
while i < 6:
  print(i)
  i += 1
#ex 2
i = 1
while i < 6:
  if i == 3:  
    break
  i += 1
#ex 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#ex 4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#PYTHON Lists
#ex 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#ex 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#ex 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#ex 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#ex 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#ex 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#ex 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#ex 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#PYTHON for loops
#ex 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
   print(x)
#ex 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#ex 3
for x in range(6):
  print(x)
#ex 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":    
    break
  print(x)

#PYTHON Tuples
#ex 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#ex 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#ex 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#ex 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#PYTHON Sets
#ex 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#ex 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#ex 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#ex 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#ex 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#PYTHON Dictionaries
#ex 1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#ex 2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
#ex 3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
#ex 4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#ex 5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#PYTHON Booleans
#ex 1
print(10 > 9)

True
#ex 2
print(10 == 9)

False
#ex 3
print(10 < 9)

False
#ex 4
print(bool("abc"))

True
#ex 5
print(bool(0))

False

#PYTHON Operators
#ex 1 
print(10 * 5)
#ex 2 
print(10 / 2)
#ex 3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#ex 4
if 5 != 10:
  print("5 and 10 is not equal")
#ex 5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

#PYTHON If...Else
#ex 1
a = 50
b = 10
if a > b:
  print("Hello World")
#ex 2
a = 50
b = 10
if a != b:
  print("Hello World")
#ex 3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")
#ex 4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
#ex 5
if a == b and c == d:
  print("Hello")
#ex 6
if a == b or c == d:
  print("Hello")
#ex 7
if 5 > 2:
  print("YES")
#ex 8
a = 2
b = 5
print("YES") if a==b else print("NO")
#ex 9
a = 2
b = 50
c = 2
if a==c or b==c: 
    print("YES")
