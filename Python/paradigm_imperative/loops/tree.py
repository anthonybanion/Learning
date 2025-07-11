# Tree
# File: tree.py
# Created: 2024-08-21
# Last Updated: 2025-06-10
# Version: 1.0.1


"""
Statement:
- Enter a number by keyboard
- print a triangle of (*)
- using the number entered as the base amount
"""

import os

number = int(input("Enter a number as the base amount: "))
os.system("clear")  # Clear the screen

print("Tree")
print("1. half of the tree")
print("2. Full tree")
print("3. Exit")
option = int(input("Enter an option: "))
if option == 1:
  for i in range(0, number):
    print("*"*(i+1))
elif option == 2:
  for i in range(0, number):
    print(" "*(number-i-1) + "*"*(2*i+1))
else:
  print("Good bye")

