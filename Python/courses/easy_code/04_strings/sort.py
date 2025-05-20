"""
Various string manipulation methods.

File: sort.py
Author: Anthony Bañon
Created: 2025-05-20
Last Updated: 2025-05-20
"""


title = '  professional python 202 course'
title = title.strip()  # removes leading and trailing whitespace
print(title.strip()) 


# converts all letters to uppercase
capital = title.upper()
print(capital)

# converts all letters to lowercase
lower = title.lower()
print(lower)


# Capitalizes the first letter of the string
capitalized = lower.capitalize()  
print(capitalized)

 
# Sort the string in alphabetical order
print('python' in lower)


# Count the number of occurrences of 'o' in the string
print(title.count('o'))


# returns the index of the first occurrence of 'o' in the string
print(title.find('o'))
print(title.find('o', 5, 10))  # starts searching from index 5 and ends at index 10


# Sort the startswith and endswith methods
print(title.startswith('Professional'))

print(title.endswith('Course'))


# returns True if the string is numeric
print('202'.isnumeric())  



