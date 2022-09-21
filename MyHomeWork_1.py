# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: \n")
## We make a string and print the type pf it which is string, we increment the string and add new statment and update it.
# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print("observations: \n")
#we craete a list of 3 number and we print the type of the list which is list, then we reach to index 0 and replace it to five then update the change.

# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: \n")
#We create a dectionry there's two variables (name and age) and one of them is the key..we print the type of decioray  and change the value of the Age from 43 to 19..
# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: \n")
#the tuple is immutable 
# # Uncomment the below code and run it, can u explain what happened?
# tuple[0] = 2
#print("observations: \n")
