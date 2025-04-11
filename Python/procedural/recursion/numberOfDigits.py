# Description: This program counts the number of digits in a number using recursion.
# File: numberOfDigits.py
# Create Date: 11/04/2025

number = input("Enter a number")

def numberOfDigits(number):
    # Base case: if the number is 0, return 1
    if number == 0:
        return 0
    # Recursive case: divide the number by 10 and call the function again
    else:
        return 1 + numberOfDigits(number // 10)

# Check if the input is a valid number
if number.isdigit():
    # Convert the input to an integer
    number = int(number)
    # Call the recursive function and print the result
    print("The number of digits in", number, "is", numberOfDigits(number))
else:
    # If the input is not a valid number, print an error message
    print("Please enter a valid number.")
# The program uses recursion to count the number of digits in a number.


    