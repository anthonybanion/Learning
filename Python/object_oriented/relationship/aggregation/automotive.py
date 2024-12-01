#Brief: Composition in Python
#Date: 05/11/2024
#Version: 1.0


#clase contenida
class Motor():
    def __init__(self, cilindros, hp):
        self.cilindros=cilindros
        self.hp=hp
    
    def __repr__(self):
        return f'el motor tiene {self.cilindros} cilindros'
    
    def trabaja(self):
        for i in range(self.hp):
            print(i, end=',')
        print()


#clase contenedora
class Auto():
    def __init__(self,modelo, precio):
        self.modelo=modelo
        self.precio=precio
        self.motor=Motor(4,100)      #hacemos la composicion

    def __repr__(self):
        return f'El auto es {self.modelo} donde {self.motor} y cuesta {self.precio}'
    
    def encender(self):
        print('El auto enciende')
        self.motor.trabaja()

#creamos un auto
auto1=Auto('Fiesta', 20000)
print(auto1)
auto1.encender()

    