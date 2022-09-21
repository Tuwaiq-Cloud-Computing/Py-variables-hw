# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: Firstly, we have return the type of the object which is string, \nThen we return the unique ID for the specific object which is 1833286480048\nAt the last we defined another string which is (from twuaiq!) and we printed its unique ID\n")

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print("observations: It is the same as the first one, the only difference here is the class of data structure which is List \n")


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: In this question we printed the type of the class which is dict and we printed its unique ID as well\nThen we printed the unique number of the age which is 43\nThen we defined the Age of Ahmed which is 19 and we printed it as well\nLastly we printed the whole unique ID of the Dict again\n")

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: Here we defined a tuple with some varibales\nThen we printed the type of the class which is tuple following by its unique ID\n")

# # Uncomment the below code and run it, can u explain what happened?
# tuple[0] = 2
#print("observations: \n")