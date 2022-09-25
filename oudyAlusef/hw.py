# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: The memory address changes as the variable changes \n")

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print("observations: All elements 'list' at the same memory address \n")


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: The memory address in the list of dictionaries does not change even if you change a value inside it \n")

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: print addres memory for 'tuple' \n")

# # Uncomment the below code and run it, can u explain what happened?
tuple[0] = 2
print("observations: object does not support item assignment \n")
