# Description: This program calculates the sum the two numbers using recursion.
# File: sum.py
# Create Date: 11/04/2025

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

def sumNumbers(number1, number2):
    # Base case: if the second number is 0, return the first number
    if number2 == 0:
        return number1
    # Recursive case: add 1 to the first number and call the function again with the second number decreased by 1
    else:
        return sumNumbers(number1 + 1, number2 - 1)
# Check if the inputs are valid numbers
if number1.isdigit() and number2.isdigit():
    # Convert the inputs to integers
    number1 = int(number1)
    number2 = int(number2)
    # Call the recursive function and print the result
    print("The sum of", number1, "and", number2, "is", sumNumbers(number1, number2))
else:
    # If the inputs are not valid numbers, print an error message
    print("Please enter valid numbers.")
# The program uses recursion to calculate the sum of two numbers.
