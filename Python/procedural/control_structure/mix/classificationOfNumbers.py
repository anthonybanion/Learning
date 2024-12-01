# Brief: Classification of numbers
# Statement:
#- Prompt the user for the amount of numbers to enter.
#- Enter each number by keyboard
#- Classify each number as positive, negative or zero
#- Prints the number of positive, negative and zero numbers entered
# Date: 20/08/2020
# Version 1.0


positive = 0
negative = 0
Zero = 0
amount = int(input("Enter the amount of numbers to classify:"))

for i in range(amount):
    numero = float(input("Enter a number: "))
    if numero>0:
        positive+=1
    elif numero<0:
        negative+=1
    else:
        Zero+=1

print("Positive numbers: ",positive)
print("Negative numbers: ",negative)
print("Zero nmbers: ",Zero)
