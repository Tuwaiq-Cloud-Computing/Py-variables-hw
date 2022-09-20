# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print((str))# delete the id 

print("observations: \n The new Sentence will be Hello world from twuaiq ")


# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print((list)) # delete the "id" to print the list after the index 0 changed
print("observations: \n The index [0] in the list will change to 5 instied of 1")


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print((my_dict))

print("observations: \n The age value will change to 19 instead of 43")

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: \n The tuple is immutable so we can not chane the values after the tuple created  ")


