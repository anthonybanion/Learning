"""
Simple list operations and slicing
 
File: lists.py
Author: Anthony Bañon
Created: 2025-05-19
Last Updated: 2025-05-19
"""



#               0       1      2      3         4        5      6    increasing
#              -7      -6      -5    -4        -3      -2      -1    decreasing
courses = ['Python', 'Java', 'Php', 'Go', 'JavaScript', 'C#', 'C++']
number = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]

print(courses[-2])  # allows negative values


last_value = courses[len(courses) - 1]
print(last_value)


# Slicing = [start:end:step]
new_list = courses[:]  # Copy the entire list
lower_sublist = courses[:2]  # The last element is not included
top_sublist = courses[4:]  # The first element is included
sublist = courses[1:5:2]  # The first element is included, the last element is not included
inverted_list = courses[::-1]  # Invert the list

print(new_list)
print(lower_sublist)
print(top_sublist)
print(sublist)
print(inverted_list)
