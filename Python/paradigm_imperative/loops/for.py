#Brief: Bucles
#Date: 05/11/2024
#Version: 1.0

"""
Statement: 
Write a program that asks the user for a word and 
displays it 10 times per screen
"""
word = input("Enter a word: ")
for i in range(1,11):
    print(f"{i}.{word}")
