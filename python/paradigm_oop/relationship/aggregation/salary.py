#Brief: Create a class that represents a salary and an employee using aggregation
#Date: 05/11/2024
#Version: 1.0

class salario:
    def __init__(self, monto):
        self.monto = monto

    def salarioAnual(self):
        return (self.monto * 12)
    
    def __del__(self):
        print('Se a eleiminado salario')

class Empleado:
    def __init__(self, nombre, edad, monto):
        self.nombre=nombre
        self.edad=edad
        self.salario=monto
    
    def get_nombre(self):
        return self.nombre
    
    def salarioEmpleado(self):
        return self.salario.salarioAnual()
    
    def __repr__(self):
        return f'El empleado {self.nombre} tiene {self.edad} años y gana {self.salario.monto}'
    
    def __del__(self):
        print('Se ha eliminado el empleado {self.nombre}')


salario1=salario(25000)
empleado1=Empleado('Juan', 35, salario1)
print(empleado1.salarioEmpleado())
del(empleado1)
# print(empleado1)
print(salario1.monto)
