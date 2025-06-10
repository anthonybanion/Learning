#Brief: Calculate the IMC
#Date: 05/11/2024
#Version: 1.0

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
IMC = peso / altura**2
print("el IMC es: ", IMC)
if IMC < 18.5:
    print("bajo peso")
elif (IMC >= 18.5) and (IMC < 24.9):
    print("Normal")
elif (IMC >= 25) and (IMC < 29.9):
    print("sobrepeso")
else :
    print("Obesidad")


