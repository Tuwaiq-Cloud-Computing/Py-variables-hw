# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: \n")
print("the function (id) changes when the value of the string variable (str) changes \n")

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(list)
print(id(list))

print("observations: \n")
print("The id for a variable of type (list) remains the same even when one of the values is changed \n")

# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: \n")
print("The id for a variable of type (dictionary) remains the same even when one of the values is changed \n")

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: \n")

print("the values of the variable (tuple) are Immutable, so no change can be made \n")

tuple [0] = 2
print("observations: \n")


