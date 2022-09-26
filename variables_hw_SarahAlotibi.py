# ---
str = "Hello world"
print(type(str))#print string is the type of Hello world
print(id(str))#print an identity integer number of Hello world
str +=  " from twuaiq!"
print(id(str))#print an identity integer number of Hello world from twuaiq

print("observations: the different id of the first str and second str \n")

# ---
list = [1,2,3]
print(type(list))#print list of integer is the type of list
print(id(list))#print an identity integer number of list
list[0] = 5
print(id(list))

print("observations: the same id of the first list and second list\n")


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))#print the type of the dict
print(id(my_dict))#print an identity integer number of the dict
print(my_dict["Age"])#print the value of Age 
my_dict["Age"] = 19 #change the value of Age
print(my_dict["Age"])#print the value of Age after update
print(id(my_dict))

print("observations: where the change of value for any key in the dict the id still the same not change\n")

# --- 
tuple = 1,2,3
print(type(tuple))#print the type of the tuple
print(id(tuple))#print an identity integer number of the tuple
tuple[0] = 2#change the value of index 0
print("observations: the tuple not accept the change in value \n")

# # Uncomment the below code and run it, can u explain what happened?
# tuple[0] = 2
#print("observations: \n")
