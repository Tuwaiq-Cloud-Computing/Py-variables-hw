# ---

str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("According to Python Docs; the ID is a unique number for the object \
during its lifetime. \
\nAdditionally, this ID is assigned when the object is created, and it is the object's memory address (w3schoofls n.d.) \
\nSo, in this code we have changed the value of the variable, therefore there will be a change in its ID.\n")

# ---


list = [1,2,3]
print(type(list))
print(id(list))
#print(id(list[0]))
list[0] = 5
print(id(list))
#print(id(list[0]))
#list[1] = 4
#print(id(list))
#list[2] = 44
#print(id(list))

print("In this code the id of the list was not changed as we only changed the value inside this list,\
 \nAlso, the change of an ID will be only for the value itself.\n")



# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
#print(id(my_dict["Age"]))
my_dict["Age"] = 19
print(my_dict["Age"])
#print(id(my_dict["Age"]))
print(id(my_dict))

print("Same with the previous one, tha change of ID will be only for the changed value inside the Dictionary: \n")

# ---
tuple = (1,2,3) # I have modified this tuple by adding the round brackets ()
print(type(tuple))
print(id(tuple))
#print(tuple[0])
print("According to (Kumar 2020); 'tuples are written with round brackets () and it can contain mixed data types.'\n")

# # Uncomment the below code and run it, can u explain what happened?
#tuple[0] = 2
print("This line is trying to modify the tuple, where tuples are immutable in nature, so they don't allow any alterations (Kumar 2020). \
\nTherefore, this code will return with an error.\n")
