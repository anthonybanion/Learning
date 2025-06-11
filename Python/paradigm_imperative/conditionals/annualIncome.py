#Brief: annual income
#Date: 05/11/2024
#Version: 1.0

"""
Statement:
write a program that asks the user for their annual 
income and displays the tax rate on the screen
reta: less than 10,000, between = 10,000 and 20,000; 
between = 20,000 and 35,000; between = 35,000 and 60,000
more than 60,000
"""


renta_anual= int(input("Enter your annual income: "))
if renta_anual < 10000:
    print("Paga 5% de impuesto")
elif renta_anual >= 10000 and renta_anual < 20000:
    print("Paga 15% de impuesto")
elif renta_anual >= 20000 and renta_anual < 35000:
    print("Paga 30% de impuesto")
elif renta_anual >= 35000 and renta_anual < 60000:
    print("Paga 45% de impuesto")