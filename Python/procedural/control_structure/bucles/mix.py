#Brief: Write a program that asks the user for a positive
#Date: 05/11/2024
#Version: 1.0

#escribir un programa, que pida al usuario un numero 
#entero positivo y muestre por pantalla todos los numeros
#impares desde 1 hasta ese numero separados por comas.
numero = int(input("Introduce un numero entero positivo: "))

for i in range(1, numero+1, 2):
    print(i, end=", ")


