#Implementar una función para calcular 
# la potencia dado dos números enteros, 
# el primero re-presenta la base y segundo el exponente

def potenciaSimple(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potenciaSimple(base, exponente - 1)
    
print(potenciaSimple(2, 4)) #16
    
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        print(f"{base ** exponente}")
        return potencia(base, exponente - 1)

print(potencia(2, 4)) #8