#Brief: Department
#Detail: The relationship between the two classes is one-to-one, where each department has a unique boss.
#Date: 06/11/2024
#Version: 1.0



class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jefe = None  # Este departamento tiene un jefe

class Jefe:
    def __init__(self, nombre):
        self.nombre = nombre

# Relación 1 a 1: un departamento tiene un jefe
jefe1 = Jefe("Carlos")
departamento = Departamento("Recursos Humanos")
departamento.jefe = jefe1

print(f"El jefe del departamento de {departamento.nombre} es {departamento.jefe.nombre}")
