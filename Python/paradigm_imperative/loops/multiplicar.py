# Multiplication Table
# File: multiplicacion.py
# Created: 2024-08-21
# Last Updated: 2025-06-10
# Version: 1.0.1

"""Statement:
- The program will ask the user for a number
- The program will print the multiplication table of that number from 1 to 12
"""
LIMIT_NUMBER = 13

number = int(input("Enter a number: "))
print("Multiplication Table")

for i in range(1, LIMIT_NUMBER):
    print(f"{number} x {i} = {number*i}")

