#Brief: Write a program that asks the user for a positive
#Date: 05/11/2024
#Version: 1.0

"""
Statement:
Write a program that prompts the user for a positive 
integer and displays all odd numbers from 1 to that number, 
separated by commas.
"""
number = int(input("Enter a positive integer: "))

for i in range(1, number+1, 2):
    print(i, end=", ")


