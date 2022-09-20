# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: \n\
    What's new here is the id() function, it's return identity number stord in memory, \
    as we saw that number changed when the value of the variable changed, so we understand \
    that each value has different id number in memory.")

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print("observations: \n\
    here we find in arrays the storage location in memory is specific and fixed, \
    and will not change with cange the value.")


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: \n\
    here also in dictionary we note the id number did not change after changing value.")

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: \n\
    here in tuple we find it dealt as one chain and stored it in one location, \
    but if we try dealing with each element one by one it will be different.")

# # Uncomment the below code and run it, can u explain what happened?
# tuple[0] = 2
print("observations: \n\
    as we learn in tuple the value it will be unmodifiable.")
