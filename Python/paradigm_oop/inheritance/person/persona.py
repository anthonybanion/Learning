#Brief: Create a class called persona
#Date: 05/11/2024
#Version: 1.0

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self, edad):
        return self.edad

persona1 = persona("Lucas", 25)

print(persona1.get_nombre())
