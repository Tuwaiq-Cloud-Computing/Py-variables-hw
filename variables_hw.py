# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

'''
First print for print know variable kind type String or int or...
then print  address  str in RAM str(immutable).
next we are use += for add sentence " from twuaiq!"  for Hello world.
after that we are print address str again.
'''
print("observations: \n")

# ---

list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))
'''
First one  we are creat list and print type if you need knew kind list.
after that print address list next step update index[0]=2 to 5.
finally print address list again.
'''
print("observations: \n")


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

'''
hi :) this is Faisal.
First step creat Dictionary key and value.
after that we are print age equle 43 next step initialize  new value for age
finally print address list.
'''
print("observations: \n")

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))


'''
.......................................................
Hello this is Faisal again :).
First step create tupe afte that initialize value,
next step print type tuple finally print address tuple.
.......................................................
Have a nice time....
'''
print("observations: \n")

# # Uncomment the below code and run it, can u explain what happened?
 #tuple[0] = 2
 # ------------------------------------------------------------------ 
 # - Error becuase tuple Immutable you can't update or change value.
 # -  also IndentationError abute space 
# ------------------------------------------------------------------

#print("observations: \n")
