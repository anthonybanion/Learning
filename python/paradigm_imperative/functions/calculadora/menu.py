# Description: Menu of the calculator
# Linked file: operations.py
# Date: 20/08/2024


from operations import *

 
def Menu(number1, number2):
    print("Calculator")
    print("1.- Addition")
    print("2.- Subtraction")
    print("3.- Multiplication")
    print("4.- División")
    print("5.- Go out")
    opcion = int(input("Select an option: "))
    if opcion == 1:
        print(addition(number1, number2))
    elif opcion == 2:
        print(subtraction(number1, number2))
    elif opcion == 3:
        print(multiplication(number1, number2))
    elif opcion == 4:
        print(division(number1, number2).__round__(2))
    elif opcion == 5:
        print("Goodbye")
    else:
        print("Invalid option")
        Menu()
