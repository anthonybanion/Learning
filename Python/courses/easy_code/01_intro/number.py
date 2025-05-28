""" 
It includes examples of string, integer, float, and boolean types.
 
File: number.py
Author: Anthony Bañon
Created: 2025-05-19
Last Updated: 2025-05-19
"""


# Constants do not exist in Python, uppercase variables are used.
CONST = 10

number=10

result= number/CONST  # 1.0 because: / It is a floating division operator
print(f"The result is: {result}")

result = number//CONST  # 1 because: // It is a floor division operator
print(f"The result is: {result}")

number = 10_000_000  # This is for readability, it is the same as 10000000
print(f"The number is: {number}")