"""
Demonstrating various tuple functions and methods.

File: tuples_function.py
Author: Anthony Bañon
Created: 2025-05-19
Last Updated: 2025-05-19
"""


numbers = (1, 4, 7, 3, 2, 9, 6, 4)


print(sorted(numbers, reverse=True))
# The sorted() function returns a new sorted list from the elements of any iterable.

print(numbers.count(4))
# The count() method returns the number of times a specified value occurs in a tuple.

print(True in numbers)
# The in operator returns (True = 1) if the specified value is present in the tuple, otherwise False.

print(numbers.index(4))
print(numbers.index(4, 2))  # Start searching from index 2
print(numbers.index(4, 1, 5))  # Start searching from index 1 to index 5