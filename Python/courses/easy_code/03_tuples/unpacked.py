# * unpacked positional arguments
tuples = (1, 2, 3)
list = [1, 2, 3]
sets = {1, 2, 3}
print(*tuples)
print(*list)
print(*sets)


# In functions
data = ['Anthony', 'Bañon']
def greet(firstname, lastname):
    print(f"Hello {firstname} {lastname}")

greet(*data) # Same as: greet('Anthony', 'Bañon')



# ** unpacked keyword arguments
# Here **person converts each key/value pair into a named argument.
person = {
'name': 'Anthony',
'age': 25
}

def show_info(name, age):
    print(f"{name} is {age} years old")

# This is the same as: show_info(name='Anthony', age=25)
show_info(**person)



# In lists and tuples: combining elements
a = [1, 2]
b = [3, 4]
combined = [*a, *b] # → [1, 2, 3, 4]
# This is the same as: combined = a + b
print(combined)

dic1 = {"x": 1}
dic2 = {"y": 2}
fusion = {**dic1, **dic2} # → {'x': 1, 'y': 2}
print(fusion)
# The ** operator unpacks the dictionary into keyword arguments.


# In multiple assignments
first, *middle, last = [1, 2, 3, 4, 5]
print(first) # 1
print(middle) # [2, 3, 4]
print(last) # 5