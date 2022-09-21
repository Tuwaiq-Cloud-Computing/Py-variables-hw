# ---
str = "Hello world"
print(type(str))
print(id(str))
str += " from twuaiq!"
print(id(str))

print("observations: \n")

#create string
#print the type of string
#print id of string
#increment the (id) string and change to from twuaiq


# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print("observations: \n")

#create list content 3 numbers
#print the type of list
#print the id of of list
#change index 0 to 5 we updated
#print id of the list


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: \n")


#create dict
#contains the dist is name and age
#print the type
#change the age number is 43 to 19
#print the id

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: \n")


#the result is error 
#Tuble are immutable


# # Uncomment the below code and run it, can u explain what happened?
# tuple[0] = 2
#print("observations: \n")