name = 'Anthony'
last_name = 'Bañon'
age = 25
is_student = True
base = 'My name is {name} {last_name} and I am {age} years old, and I am a student: {is_student}'

# The format() method replaces the placeholders in the string with the values passed as arguments
full_name1 = base.format(
    name=name, 
    last_name=last_name, 
    age=age,
    is_student=is_student
)
print(full_name1)


# The format() method can take a dictionary as an argument
full_name2 = base.format(
    **{
        'name': name, 
        'last_name': last_name, 
        'age': age,
        'is_student': is_student
    }
)
print(full_name2)


# The format() method can take a list as an argument
numbered_base = 'My name is {0} {1} and I am {2} years old, and I am a student: {3}'
full_name3 = numbered_base.format(
    *[
        name, 
        last_name, 
        age,
        is_student
    ]
)
print(full_name3)


# The format() method can take a tuple as an argument
full_name4 = numbered_base.format(
    *(
        name, 
        last_name, 
        age,
        is_student
    )
)
print(full_name4)


# The format() method can take a set as an argument 
# NOT RECOMENDED
full_name5 = numbered_base.format(
    *{
        name, 
        last_name, 
        age,
        is_student
    }
)
print(full_name5)


# The format() method can take a string as an argument
full_name6 = numbered_base.format(
    'Anthony', 
    'Bañon', 
    25,
    True
)
print(full_name6)


# The format() method can take a boolean as an argument
bool_base = 'Values: {0}, {1}, {2}'
full_name7 = bool_base.format(
    True, 
    False, 
    True
)
print(full_name7)

