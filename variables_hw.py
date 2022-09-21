# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: \n id changed after changing the value of the variable")

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print("observations: \n id did not change after changing the value of the variable inside the list")


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: \n id did not change after changing the value of key inside the dictionary")

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: \n if we named the variable tuple we don't need to use () to make it a tuple")

# # # Uncomment the below code and run it, can u explain what happened?
# # tuple[0] = 2
# #print("observations: \n tuple is imutable we cant modify it")

