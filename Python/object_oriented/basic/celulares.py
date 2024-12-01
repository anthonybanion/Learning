#Brief: Create a class called celulares
#Date: 05/11/2024
#Version: 1.0

class celulares:
    def __init__(self, marca, modelo, capacidad):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad
    
    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo
    
    def get_capacidad(self):
        return self.capacidad
    
    def set_marca(self, marca):
        self.marca = marca
    
    def set_modelo(self, modelo):
        self.modelo = modelo
    
    def set_capacidad(self, capacidad):
        self.capacidad = capacidad
    

nokia=celulares("Nokia", "1100", "32MB")
samsung=celulares("Samsung", "Galaxy S10", "128GB")
alcatel=celulares("Alcatel", "1", "16GB")

print(nokia.get_marca(), nokia.get_modelo(), nokia.get_capacidad())

nokia.set_marca("Motorola")
nokia.set_modelo("Moto G")
nokia.set_capacidad("64GB")

print(nokia.get_marca(), nokia.get_modelo(), nokia.get_capacidad())