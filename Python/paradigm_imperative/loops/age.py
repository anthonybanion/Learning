#Brief: Write a program that asks the user for their age
#Date: 05/11/2024
#Version: 1.0

"""
Statement:
write a program that asks the user for their age
displays on the screen all the years they have completed (from 1 to their age).
"""

age = int(input("Enter your age: "))
for i in range(1, age+1):
    print(f"You have completed {i} years")
