"""
Demonstrates the use of different data types in Python.
 
File: dataTypes.py
Author: Anthony Bañon
Created: 2025-05-19
Last Updated: 2025-05-19
"""


first_name = input("Enter your first name: ")  #str
age = int(input("Enter your age: "))  #int
height = float(input("Enter your height: "))  #float
is_married = input("He is married? (yes/no): ") == "yes"  #bool

print("Your name is " + first_name)
print("Your age is " + str(age))
print("Your height is " + str(height))
print("Your marital status is " + str(is_married))


print(type(first_name))  #<class 'str'>
print(type(age))  #<class 'int'>
print(type(height))  #<class 'float'>
print(type(is_married))  #<class 'bool'>

#Multiple variables
first_name, age, height, is_married = input("Enter your first name, age, height and marital status (yes/no): ").split(",")
age = int(age)  # Convert age to int
height = float(height)  # Convert height to float
is_married = is_married.strip().lower() == "yes"  # Convert is_married to bool
print(first_name)
print(age)
print(height)
print(is_married)