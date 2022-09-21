# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: \n")
# create and assign a value to the variable "str" 
# printing type , id and increment the variable "str" 

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print("observations: \n")
# create a list that consist of 3 items
# printing type and id of list 
# change the value of item 0 from 1 to 5 and printing id of list *the id doesn't change when the value of item is changed*


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: \n")
# create dictionary that consist of 2 keys with their values
# printing type and id of dictionary and the key "Age"
# change the value of "Age" from 43 to 19 and print it , also print the id of dictionary

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: \n")
# create a tuple that consist of 3 values and print the type and id of tuple

# # Uncomment the below code and run it, can u explain what happened?
tuple[0] = 2
print("observations: \n")

#TypeError , because tuples are immutable and we use it when we want to store a list of values that wont be editing.
