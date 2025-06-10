# Title: Multiplication Table
#- Enter a number by keyboard
#- print the multiplication table of the number entered
# Date: 21/08/2024
# Version: 1.0


LIMIT_NUMBER = 13

number = int(input("Enter a number: "))
print("Multiplication Table")

for i in range(1, LIMIT_NUMBER):
    print(f"{number} x {i} = {number*i}")

