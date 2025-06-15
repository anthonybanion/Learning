# Game 21
# File: game21.py
# Created: 2024-11-05
# Last Updated: 2025-06-10
# Version: 1.0.1

import random as rd

LOWER_LIMIT = 1
HIGH_LIMIT = 13

sum1=0
sum2=0
card5=0
card6=0

print("GAME 21")
print("The user and the machine receive two random cards")
card1 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
card2 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
print("First card: ", card1 )
print("Second card: ", card2 )
sum1 = card1 + card2
print("User sum: ", sum1)


card3 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
card4 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
sum2 = card3 + card4


while sum1 < 21:
    print("Deseas pedir una card adicional? (s/n)")
    respuesta = input()
    if respuesta == "s":
        card5 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
        print("card adicional usuario: ", card5 )
        sum1 = sum1 + card5
        print("sum usuario: ", sum1)
    else:
        break

while sum2 < 17:
    if sum2 < 17:
        card6 = rd.randint(LOWER_LIMIT, HIGH_LIMIT)
        sum2 = sum2 + card6
    else:
        break

if sum1 > 21:
    print("El usuario ha perdido")
elif sum2 > 21:
    print("El maquina ha perdido")
elif sum1 == 21:
    print("El usuario ha ganado")
elif sum2 == 21:
    print("El maquina ha ganado")
else:
    if sum1 > sum2:
        print("El usuario ha ganado")
    else:
        print("El maquina ha ganado")

print("Fin del juego")
print("usuario: ",card1, card2, card5,"La sum es: ",sum1)
print("maquina: ", card3, card4, card6,"La sum es: ", sum2)