# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: After identifing the strings have changed it and that's results to change the ID in the memory \n")

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print("observations: we change the value from index number [0] to [5] and the leads to change the memory \n")


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: using the key word age to change the value to 43 and the ID has not been changed because same number of elements   \n")

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: printed the type of tuple and ID \n")

# # Uncomment the below code and run it, can u explain what happened?
#tuple[0] = 2
print("observations: syntax error becuase tuple immutable \n")
