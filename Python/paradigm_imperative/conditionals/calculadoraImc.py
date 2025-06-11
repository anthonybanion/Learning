#Calculate the IMC
#File: calculadoraImc.py
#Created: 2024-11-05
#Last Updated: 2025-06-10
#Version: 1.0.1

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
IMC = weight / height**2
print("BMI is: ", IMC)
if IMC < 18.5:
    print("underweight")
elif (IMC >= 18.5) and (IMC < 24.9):
    print("Normal")
elif (IMC >= 25) and (IMC < 29.9):
    print("overweight")
else :
    print("Obesity")


