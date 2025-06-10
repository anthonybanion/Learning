#Brief: Write a program that asks the user for their age
#Date: 05/11/2024
#Version: 1.0

#escribir un programa que pregunte al usuario su edad
#muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input("Introduce tu edad: "))
for i in range(1, edad+1):
    print(f"Has cumplido {i} años")
