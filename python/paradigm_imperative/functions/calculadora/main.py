# Brief: Calculator
# Date: 20/08/2024
# Linked file: menu.py
# Version: 1.0

"""
Statement:
This program performs basic arithmetic operations
It prompts the user for two numbers and an operation
It then displays the result of the operation
"""

from menu import Menu

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

Menu(number1, number2)