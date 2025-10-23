#Implementar una función para calcular el producto de dos números enteros dados.


def multiplicacion(a):
    if a <= 0:
        return 0
    else: 
     resultado=  a * 2
     print(f"2 x {a} = {resultado}")
    return multiplicacion(a-1) 

print(multiplicacion(10))

def division(a):
    if a <= 0:
        return 0
    else: 
     resultado=  a / 2
     print(f"{a} / 2 = {resultado}")
    return division(a-1)    

print(division(10))