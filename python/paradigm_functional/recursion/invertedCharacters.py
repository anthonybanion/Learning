# Description: Invert characters in a string using recursion.
# File: invertedCharacters.py
# Create Date: 11/04/2025

string = input ("Enter a string")
def invertedCharacters(string):
    # Base case: if the string is empty, return an empty string
    if len(string) == 0:
        return ""
    # Recursive case: get the last character and call the function again with the rest of the string
    else:
        return string[-1] + invertedCharacters(string[:-1])
# Check if the input is a valid string
if isinstance(string, str):
    # Call the recursive function and print the result
    print("The inverted string is:", invertedCharacters(string))
else:
    # If the input is not a valid string, print an error message
    print("Please enter a valid string.")
    
