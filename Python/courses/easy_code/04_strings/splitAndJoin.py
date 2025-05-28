"""
Split and join strings examples
 
File: splitAndJoin.py
Author: Anthony Bañon
Created: 2025-05-20
Last Updated: 2025-05-20
"""


#split -> list
# The split() method splits a string into a list of substrings
# The default separator is whitespace
courses = 'Python Java Php Go C# C++ Ruby on Rails'
print(courses.split())


# The split() method can take a separator as an argument
courses = 'Python, Java, Php, Go, C#, C++, Ruby on Rails'
print(courses.split(', '))  # use , and whitespace as separator


# The split() method will split the string into a maximum of 2 substrings
print(courses.split(',', 2))


#join -> string
# The join() method joins a list of strings into a single string
print(', '.join(['Python', 'Java', 'Php', 'Go', 'C#', 'C++']))


# The join() method takes a separator as an argument
print(' - '.join(['Python', 'Java', 'Php', 'Go', 'C#', 'C++']))


# The join() method returns a string
print(''.join(['Python', 'Java', 'Php', 'Go', 'C#', 'C++']))
# The join() method can be used to join a list of strings into a single string      