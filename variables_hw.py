# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: \n")

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print("observations: \n")


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: \n")

# --- 
tuple = 1,2,3
tuple[0] = 2
print(type(tuple))
print(id(tuple))

print("observations: \n")

# # Uncomment the below code and run it, can u explain what happened?
#print("observations: \n")
## An Error because the tuple is  immutable.
