"""
Demonstrates the use of comparison and logical operators in Python.
 
File: operator.py
Author: Anthony Bañon
Created: 2025-05-19
Last Updated: 2025-05-19
"""


number_one = 10
number_two = 20

result = number_one == number_two  # False because: == It is a comparison operator
print(f"The result is: {result}")

result = number_one != number_two  # True because: != It is a comparison operator
print(f"The result is: {result}")

result  = True and True and number_one == number_two 
print(f"The result is: {result}")  

# To make code jumps use ()
result  = (
    True
    and True
    and number_one != number_two
    or number_one > 100
    and number_two < 50
    )

result = not (
    (number_one != number_two)
    and (number_one > 100)
    and (number_two < 50)
    )
print(f"The result is: { not result}")  