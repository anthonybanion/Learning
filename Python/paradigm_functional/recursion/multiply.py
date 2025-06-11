# Description: This function performs multiplication using recursion.
# File: multiply.py
# Create Dtae: 11/04/2025

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

def multiply(number1, number2):
    # Base case: if the second number is 0, return 0
    if number2 == 0:
        return 0
    # Recursive case: add the first number to the result of multiplying the first number with the second number decreased by 1
    else:
        return number1 + multiply(number1, number2 - 1)
# Check if the inputs are valid numbers
if number1.isdigit() and number2.isdigit():
    # Convert the inputs to integers
    number1 = int(number1)
    number2 = int(number2)
    # Call the recursive function and print the result
    print("The product of", number1, "and", number2, "is", multiply(number1, number2))
else:
    # If the inputs are not valid numbers, print an error message
    print("Please enter valid numbers.")    
# The program uses recursion to calculate the product of two numbers.