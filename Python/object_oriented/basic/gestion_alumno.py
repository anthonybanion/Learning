#Brief: Gestion de alumnos
#Date: 05/11/2024
#Version: 1.0

class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.dni}'

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_dni(self):
        return self.dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_dni(self, dni):
        self.dni = dni

class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, legajo):
        super().__init__(nombre, apellido, dni)
        self.legajo = legajo

    def __str__(self):
        return f'{super().__str__()} {self.legajo}'

    def get_legajo(self):
        return self.legajo

    def set_legajo(self, legajo):
        self.legajo = legajo

    def presentarse(self):
        return f'Hola soy {self.nombre} {self.apellido} y mi legajo es {self.legajo}'
    
class Profesor(Persona):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)

    def __str__(self):
        return f'{super().__str__()} {self.materia}'

    def presentarse(self):
        return f'Hola soy {self.nombre} {self.apellido} y doy la materia {self.materia}'

class Materia:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'{self.nombre}'

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

class Nota:
    def __init__(self, nota):
        self.nota = nota