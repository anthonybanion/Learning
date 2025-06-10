#Brief: Create a class called automotor
#Date: 05/11/2024
#Version: 1.0


class automotor:
    def __init__(self, marca, modelo, cantidad_puertas, cantidad_combustible, kilometro):
        self.marca = marca
        self.modelo = modelo
        self.cantidad_puertas = cantidad_puertas
        self.cantidad_combustible = cantidad_combustible
        self.kilometro = kilometro

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.cantidad_puertas} {self.cantidad_combustible} {self.kilometro}"

    def get_marca(self):
        return self.marca
    def get_modelo(self):
        return self.modelo
    def get_cantidad_puertas(self):
        return self.cantidad_puertas
    def get_cantidad_combustible(self):
        return self.cantidad_combustible
    def get_kilometro(self):
        return self.kilometro
    
    def set_marca(self, marca):
        self.marca = marca
    def set_modelo(self, modelo):
        self.modelo = modelo
    def set_cantidad_puertas(self, cantidad_puertas):
        self.cantidad_puertas = cantidad_puertas
    def set_cantidad_combustible(self, cantidad_combustible):
        self.cantidad_combustible = cantidad_combustible
    def set_kilometro(self, kilometro):
        self.kilometro = kilometro

  
    def carga_combustible(self, cantidad_combustible):
        self.cantidad_combustible += cantidad_combustible
        print(f"Usted cargo: {cantidad_combustible} litros")
    
carga = float(input("¿Cuanto combustible quiere cargar: ?"))

auto1=automotor("toyota","24",4,50,0)
auto1.carga_combustible(carga)