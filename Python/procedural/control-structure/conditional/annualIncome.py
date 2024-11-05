#Brief: annual income
#Date: 05/11/2024
#Version: 1.0

#escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo 
#de impuesto que le toca
# reta : menos= 10.000, entre = 10.000 y 20.000; entre= 20.000 y 35.000; entre= 35.000 y 60.000
#mas de 60.000

renta_anual= int(input("Ingrese su renta anual: "))
if renta_anual < 10000:
    print("Paga 5% de impuesto")
elif renta_anual >= 10000 and renta_anual < 20000:
    print("Paga 15% de impuesto")
elif renta_anual >= 20000 and renta_anual < 35000:
    print("Paga 30% de impuesto")
elif renta_anual >= 35000 and renta_anual < 60000:
    print("Paga 45% de impuesto")