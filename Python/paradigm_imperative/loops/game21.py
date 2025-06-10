#Brief: Game 21
#Date: 05/11/2024
#Version: 1.0

import random as rd

LOWER_LIMIT = 1
HIGH_LIMIT = 13

suma1=0
suma2=0
carta5=0
carta6=0

print("JUEGO 21")
print("El usuario y la maquina reciben dos cartas aleatorias")
carta1 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
carta2 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
print("Primera carta: ", carta1 )
print("Segunda carta: ", carta2 )
suma1 = carta1 + carta2
print("Suma usuario: ", suma1)


carta3 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
carta4 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
suma2 = carta3 + carta4


while suma1 < 21:
    print("Deseas pedir una carta adicional? (s/n)")
    respuesta = input()
    if respuesta == "s":
        carta5 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
        print("Carta adicional usuario: ", carta5 )
        suma1 = suma1 + carta5
        print("Suma usuario: ", suma1)
    else:
        break

while suma2 < 17:
    if suma2 < 17:
        carta6 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
        suma2 = suma2 + carta6
    else:
        break

if suma1 > 21:
    print("El usuario ha perdido")
elif suma2 > 21:
    print("El maquina ha perdido")
elif suma1 == 21:
    print("El usuario ha ganado")
elif suma2 == 21:
    print("El maquina ha ganado")
else:
    if suma1 > suma2:
        print("El usuario ha ganado")
    else:
        print("El maquina ha ganado")

print("Fin del juego")
print("usuario: ",carta1, carta2, carta5,"La suma es: ",suma1)
print("maquina: ", carta3, carta4, carta6,"La suma es: ", suma2)