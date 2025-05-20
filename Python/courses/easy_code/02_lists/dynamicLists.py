"""
This script demonstrates dynamic list operations.

File: dynamicLists.py
Author: Anthony Bañon
Created: 2025-05-19
Last Updated: 2025-05-19
"""


courses = ['Python', 'Java', 'Php', 'Go', 'C#', 'C++']
courses.append('Ruby')  # Add an element to the end of the list
print(courses)


position = courses.index('Java')  # Get the index of an element
courses.insert(position, 'C')  # Insert an element at a specific position
print(courses)


courses.remove('C')  # Remove an element from the list by value
print(courses)


new_language = ['Pascal', 'Cobol']
courses.extend(new_language)  # Add multiple elements to the list
print(courses)


last_element = courses.pop()  # Remove the last element from the list
print(courses)
print(last_element)  # pop returns the last element
element = courses.pop(position)  # Remove an element from the list by index
print(courses)
print(element)  # pop returns the removed element


print('Pascal' in courses)  # Check if an element is in the list
print('JavaScript' in courses)


number = [0, 6, 7, 3, 1, 5, 2, 4, 8, 9]
number_copy = number.copy()  # Copy the list
print(number_copy)

number.sort(reverse=True)  # Sort the list
print(number)



courses.reverse()  # Reverse the list
print(courses)


courses.clear()  # Clear the list
print(courses)
# courses = []  # Create an empty list
