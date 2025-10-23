#Pizza
#File: pizza.py
# Created: 2024-11-05
# Last Updated: 2024-11-05
#Version: 1.0.1

"""
Statement:
The pizzeria offers vegetarian or non-vegetarian pizza.
The ingredients for each type of pizza are:
Vegetarian ingredients: bell pepper and tofu
Non-vegetarian: pepperoni, ham, and salmon
Write a program that asks the user if they want a vegetarian pizza and, based on their answer, shows them a menu with the ingredients.
They can only choose one ingredient besides the tomato and mozzarella, which are on every pizza.
At the end, the screen should show whether the pizza is vegetarian or not, along with all the ingredients it contains.
"""

option1 = int(input("What type of pizza do you want: \n 1) Vegetarian \n 2) Non-vegetarian \n Enter a topping:"))
if (option1 == 1):
    ingredient = input(" Ingredients \n 1) Pepper\n 2) Tofu \n Enter an ingredient:")
    tipo_pizza = "vegetarian"
elif (option1 == 2):
    ingredient = input(" Ingredients \n 1) Pepperoni\n 2) Ham\n 3) Salmon \n Enter an ingredient: ")
    tipo_pizza = "non-vegetarian"