#
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))


print("observations: \
    In The (3) line we've printed the type of str value, (4) line printed the id of the str var, then in (5) line we have added/ incremented the first string by adding new statement, then we've checked the id (ID:Changed not the same)")

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5     # Changed index 0 with a value of 1 to value of 5
print(id(list))


print("observations: \n  In The (14) line we've printed the type of the list value, (15) line printed the id of the list var, then in (16)  Changed index 0 with a value of 1 to value of 5, (16) then we've checked the id (ID:Changed not the same)")



# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: \n  In The (26) line we've printed the type of the list value, (27) line printed the id of the my_dict var, then in (28) we've printed the age key which is 43, (29) we've changed the age pair to 19,then in (30)we've printed the value of the age,  finally in line (31) we've checked the id (ID:Changed not the same)")

# ---
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: \n In The (36) created tuple variable with values, (37) line printed the type of the tuple var, then in (38)  finally in line we've checked the id")

# # Uncomment the below code and run it, can u explain what happened?
# tuple[0] = 2
print("observations: \n ERROR Can not change the value in tuple ('tuple' object does not support item assignment) ")


