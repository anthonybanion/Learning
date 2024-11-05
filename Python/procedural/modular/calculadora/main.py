# Brief: Calculator
# Statement:
#- Ask the user for two numbers
#- Ask the user for the operation to perform
#- Perform the operation
#- Show the result
# Date: 20/08/2024
# Linked file: menu.py
# Version: 1.0


from menu import Menu

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

Menu(number1, number2)