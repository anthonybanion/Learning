"""
Using the zip() function to combine multiple iterables
into a single iterable of tuples.

File: collections.py
Author: Anthony Bañon
Created: 2025-05-19
Last Updated: 2025-05-19
"""



users = ['John', 'Maria', 'Jose']
courses = ('Python', 'Java', 'Php', 'Go', 'C++')

 # The zip() function combines two or more iterables into a single iterable of tuples
response_list = list(zip(users, courses))
print(response_list)

response_tuple = tuple(zip(users, courses))
print(response_tuple)

response_set = set(zip(users, courses))
print(response_set)
