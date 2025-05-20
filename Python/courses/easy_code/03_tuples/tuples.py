"""
Demonstrating tuple creation, indexing, and unpacking.

File: tuples.py
Author: Anthony Bañon
Created: 2025-05-19
Last Updated: 2025-05-19
"""


#              0          1     2
#             -3         -2     -1
settings = ('localhost', 8080, True)
# The tuples are immutable, meaning they cannot be changed after creation.  
# However, you can access their elements using indexing.

print(settings[0])
print(settings[-1])

print(settings[0:2])

number = 1, 2, 3, 4, 5  # The tuple can be created without parentheses
print(number)
print(type(number))

# The tuple can be created with the tuple() constructor
number2 = tuple([1, 2, 3, 4, 5])
print(number2)
print(type(number2))

# The tuple can be unpacked into variables
a, b, c, d, e = number
print(a)
print(b)
print(c)
print(d)
print(e)




lenguages = 'Python', 'Java', 'Php', 'Go', 'C#', 'C++'
var1, _, var3, _, var5, _ = lenguages
# The underscore (_) is used to ignore the values
print(var1)
print(var3)
print(var5)


lenguages = 'Python', 'Java', 'Php', 'Go', 'C#', 'C++'
start, *middle, end = lenguages
# The asterisk (*) is used to unpack the middle values
print(start)
print(middle)
print(end)

# The tuple can be converted to a list
lenguages = list(lenguages)
print(lenguages)
# The tuple can be converted to a set
lenguages = set(lenguages)
print(lenguages)
