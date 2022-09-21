# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print('''observations:output for line 3 it give type of str variable which string because i use type function  \n output of line 4 
it give me location of variable str in memory because i use id function  \n
output for line 6 location of variable str but as i see id was change becuase line 5 we add string to variable str \n ''')

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print('''observations: output of line 14 it give type of variable list which list as i see because i use type function \n
output of line 15 it give me location of variable list in memory because i use id function \n
output for line 17 location of variable list but as i see id was change becuase line 16 we  change value for index 0 to variable list 
\n''')


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print('''observations: output of line 27 it give type of variable my_dict which dictionary as i see because i use type function \n
output of line 28 it give me location of variable my_dict in memory because i use id function \n
output of line 29 it give me 43 because in my_dict the key age has value 43 \n
output of line 31 is 19 and we notice change from 43 to 19 becuase in the line 30 we change the value for key age to 19 \n
 output of line 32 give the id of location of variable in the memory as we see same id as line 28 as lon as the value change of id age 
 because only object that saved is key not the value /n''')


# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print('''observations: output of line 44 it give type of variable tuple which also tuble  as i see because i use type function\n
utput of line 45 it give me location of variable tuple in memory because i use id function\n
''')

# # Uncomment the below code and run it, can u explain what happened?
tuple[0] = 2
print('''observations: it was error because tuple has attribute that you cant change the value inside the tuple after you insert in 
also you cant use this charichtar [] with tuples its belong to list \n''')
