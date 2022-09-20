# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: \n")

# ---
list1 = [1,2,3]
print(type(list1))
print(id(list1))
list1[0] = 5
print(id(list1))

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
tuple1 = ('1','2','3')
print(type(tuple1))
print(id(tuple1))

y = list (tuple1)
y.remove('1')
tuple1 = tuple(y)

print(id(tuple1))

print("observations: \n")

#tuple[0] = 2

# # Uncomment the below code and run it, can u explain what happened?
#tuple[0] = 2
#print("observations: \n")

'''
when you create  a tuple it's values can't be change unlike the others 
but you can change it by convert it into a list change the values
 then convert back to tuple
'''
