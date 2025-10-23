# Description: This script calculates the sum of digits in a number using recursion.
# File: sunOfDigits.py
# Create Date: 11/04/2025

number = input("Enter a number: ")

def sumOfDigits(number):
    # Base case: if the number is 0, return 0
    if number == 0:
        return 0
    # Recursive case: add the last digit to the sum of the remaining digits
    else:
        return number % 10 + sumOfDigits(number // 10)
# Check if the input is a valid number
if number.isdigit():
    # Convert the input to an integer
    number = int(number)
    # Call the recursive function and print the result
    print("The sum of digits in", number, "is", sumOfDigits(number))
else:
    # If the input is not a valid number, print an error message
    print("Please enter a valid number.")