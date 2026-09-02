# LISTS

fruits = ["apple", "banana", "cherry"] 
print(fruits) 
print(type(fruits))

# indexing - accesing one item 
print(fruits[0]) 
print(fruits[-1])

#slicing - Accesing a range
print(fruits[0:2])

#changing items - lists are mutable 
fruits[1] = "blueberry" 
print(fruits)

#common list methods
fruits.append("mango") # add to the end 
fruits.insert(1, "kiwi") # insert at a specific position
fruits.remove("apple") # remove by value 
print(fruits) 
last = fruits.pop() # remove AND return the last item 
print(last, fruits) 
print(len(fruits)) # number of items 
fruits.sort() # sort in place 
print(fruits)

#looping through a list
for fruit in fruits:
    print (fruit)

#-------------------------------------------------------------------------

# TUPPLE

#creating a tupple
point = (10,20,30)
print(point)
print(type(point))

# indexing a tupples
print(point[0])

#tupples are immutable
point[0] = 99

#tupple unpacking
x, y, z = point 
print(x, y, z)

#--------------------------------------------------------------------------

#DICTIONARIES

#creating a dictionary 
student = {"name": "Aditya", "marks": 97}
print(student)
print(type(student))

#accesing values
print(student["name"]) 
print(student.get("marks")) 
print(student.get("age"))
print(student["age"]) # direct print gives error, therfore it is preferrable to use get function

#adding and updating values
student["age"] = 20 # new key → added 
student["marks"] = 98 # existing key → updated 
print(student)

#removing a key 
del student["age"]
print(student)

#looping through a dictionary 
for key, value in student.items(): 
    print(key, ":", value)

# usefull dictionary methods
print(student.keys()) 
print(student.values()) 
print(len(student))

#----------------------------------------------------------------------------

#PUTTING THEM TOGETHER

students = [ 
    {"name": "Aarav", "marks": [88, 92, 79]}, 
    {"name": "Priya", "marks": [76, 81, 85]}, 
    ] 
for s in students: 
    avg = sum(s["marks"]) / len(s["marks"]) 
    print(s["name"], avg)

#----------------------------------------------------------------------------