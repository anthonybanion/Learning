#Brief: Department
#Detail: The relationship between the two classes is one-to-many, where each department has many employees.
#Date: 06/11/2024
#Version: 1.0

#clase contenida
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []  # Lista de empleados

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)


# Relación 1 a muchos: un departamento tiene muchos empleados
departamento = Departamento("Ventas")
empleado1 = Empleado("Juan")
empleado2 = Empleado("Ana")

departamento.agregar_empleado(empleado1)
departamento.agregar_empleado(empleado2)

for empleado in departamento.empleados:
    print(f"{empleado.nombre} trabaja en el departamento de {departamento.nombre}")
