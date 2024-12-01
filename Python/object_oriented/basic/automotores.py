import os
import time

class automotor:
    def __init__(self, marca, modelo, cant_puertas, cant_combustible, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.cant_puertas = cant_puertas
        self.cant_combustible = cant_combustible
        self.kilometraje = kilometraje

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Cantidad de puertas: {self.cant_puertas}, Cantidad de combustible: {self.cant_combustible}, Kilometraje: {self.kilometraje}"

    def cargar_combustible(self, cantidad):
        self.cant_combustible += cantidad
        return f"La cantidad de combustible es: {self.cant_combustible}"
    
    def arrancar_auto(self):
        if self.cant_combustible > 0:
            print("El auto arrancó")
        else:
            print("No hay combustible")
    
    def andar_100km_ciudad(self):
        if self.cant_combustible >= 10:
            self.cant_combustible -= 10
            self.kilometraje += 100
        else:
            print("No hay combustible")
        return f"La cantidad de combustible es: {self.cant_combustible} y el kilometraje es: {self.kilometraje}"
    
    def andar_100km_ruta(self):
        if self.cant_combustible >= 8:
            self.cant_combustible -= 8
            self.kilometraje += 100
        else:
            print("No hay combustible")
        return f"La cantidad de combustible es: {self.cant_combustible} y el kilometraje es: {self.kilometraje}"

    def autonomia_ciudad(self):
        autonomia = self.cant_combustible * 10
        return f"La autonomía en ciudad es de: {autonomia} km"
    
    def autonomia_ruta(self):
        autonomia = self.cant_combustible * 12.5
        return f"La autonomía en ruta es de: {autonomia} km"


auto = automotor("Ford", "Fiesta", 4, 90, 200)
          
cantidad = int(input("Ingrese la cantidad de combustible: "))
auto.cargar_combustible(cantidad)
print(auto.cargar_combustible(cantidad))
auto.arrancar_auto()
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla

print(''' Ruta o Ciudad
        1. Andar 100 km en ciudad
        2. Andar 100 km en ruta
        3. No hacer nada
        ingresa una opción: ''')
opcion = int(input())

if opcion == 1:
    print(auto.andar_100km_ciudad())
   
elif opcion == 2:
    print(auto.andar_100km_ruta())
else:
    print("No se realizó ninguna acción")

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear') 

print(''' Autonomia en Ciudad o Ruta
        1. Autonomia en Ciudad
        2. Autonomia en Ruta
        3. No consultar nada
        ingresa una opción: ''')
opcion = int(input())

if opcion == 1:
    print(auto.autonomia_ciudad())

elif opcion == 2:
    print(auto.autonomia_ruta())    

else:
    print("No se realizó ninguna acción")
    