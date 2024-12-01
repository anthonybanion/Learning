#Brief: Inheritance in Python
#Date: 05/11/2024
#Version: 1.0


from abc import abstractmethod
class Persona:
    def __init__(self, nombre, apellido, dni, edad):  #constructor
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.__edad = edad

    def __str__(self):  #sobrecarga de operadores
        return f'{self.nombre} {self.apellido} {self.dni}{ self.__edad}'
    
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_dni(self):
        return self.dni
    
    def get_edad(self):
        return self.edad
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_dni(self, dni):
        self.dni = dni

    def set_edad(self, edad):
        self.__edad = edad
    
    #metodo perzonalizados

    def hablar(self):
        return f'Hola soy {self.nombre} {self.apellido} y tengo {self.edad} años'
    
    def esMayor(self):
        if self.__edad > 18:
            return True
        else:
            return False
    
    def presentarse(self):
        return f'Hola soy {self.nombre} {self.apellido}'

class Habilidad:
    @abstractmethod
    def cantar(self):
        pass
    @abstractmethod
    def bailar(self):
        pass
        

class Empleado(Persona, Habilidad):
    def __init__(self, nombre, apellido, dni, edad, sueldo, antiguedad, legajo):
        super().__init__(nombre, apellido, dni, edad,)
        self.sueldo = sueldo
        self.antiguedad = antiguedad
        self.legajo = legajo

    def __str__(self):
        return f'{super().__str__()} {self.sueldo} {self.antiguedad} {self.legajo}'

    def get_sueldo(self):
        return self.sueldo

    def set_sueldo(self, sueldo):
        self.sueldo = sueldo
    
    #metodo perzonalizados
    def hablar(self):
        return super().hablar() + 'con antiguedad'+ str(self.antiguedad) + 'y sueldo'+ str(self.sueldo)
    
    def vacaciones(self):
        if self.antiguedad > 5:
            return 'Tiene vacaciones'
        else:
            return 'No tiene vacaciones'
        
    def bonificacion(self):
        if self.antiguedad > 5:
            return self.sueldo * 0.1
        else:
            return self.sueldo * 0.05
    
    def cantar(self):
        return 'Canta empleado'
    
    def bailar(self):
        return 'Baila empleado'


class Aministrador(Persona, Habilidad):
    def __init__(self, nombre, apellido, dni, edad, cargo):
        super().__init__(nombre, apellido, dni, edad,)
        self.cargo = cargo

    def __str__(self):
        return f'{super().__str__()} {self.cargo}'

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo
    

    def hablar(self):
        return super().hablar() + ' y soy un administrador'
    
    def cantar(self):
        return 'Canta administrador'
    
    def bailar(self):
        return 'Baila administrador'


class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, edad, legajo, carrera, anio):
        super().__init__(nombre, apellido, dni, edad,)
        self.legajo=legajo
        self.carrera=carrera
        self.anio=anio
    def __str__(self):
        return f'{super().__str__()} {self.legajo} {self.carrera} {self.anio}'
    
    

Alumno1=Alumno("mario", "Prez", "23423", 45, "2423", "analista", 456)
print(Alumno1)






persona1=Empleado('Juan', 'Perez', 12345678, 30, 50000, 5, 1234)

persona2=Aministrador("Perez", "Juan", 12345678, 30, 'Gerente')

persona1.__edad=25

print(persona1)

print(persona2)

print(persona1.bailar())
print(persona2.bailar())
print(persona1.cantar())
print(persona2.cantar())



if persona1.esMayor():
    print('Es mayor de edad')   