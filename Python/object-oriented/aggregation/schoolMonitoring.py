class Persona:
    def __init__ (self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, value):
        self.apellido = value

    def get_edad(self):
        return self.edad

    def set_edad(self, value):
        self.edad = value

    def get_dni(self):
        return self.dni

    def set_dni(self, value):
        self.dni = value

    def __str__ (self):
        return f"Nombre: {self.nombre}\nApellido {self.apellido}\nEdad: {self.edad}\nDNI: {self.dni}\n"

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, dni, legajo):
        super().__init__(nombre, apellido, edad, dni)
        self.legajo = legajo
        self.materias_notas = []  # Lista donde creo una tupla (materia,nota)

    def agregar_materia_nota(self, materia, nota):
        self.materias_notas.append((materia, nota)) #Aca asigna como tupla
        print(f"Materia {materia.get_nombre()} con nota {nota} asignada al alumno {self.nombre}.")

    def consultar_materias_notas(self):
        return [f"{materia.get_nombre()}: {nota}" for materia, nota in self.materias_notas]
        #materia y nota son los parametros de la funcion, lo que hace es obtener el nombre y nota,
        #despues hace el for en materia y nota, dentro de la lista materias.


    def get_legajo(self):
        return self.legajo
   
class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, dni, legajo,materias):
        super().__init__(nombre, apellido, edad, dni)

        self.legajo = legajo
        self.materias = []
    def get_legajo(self):
        return self.legajo

    def asignar_materias(self, nombre, resolucion ):
        nueva_materia = Materias(nombre, resolucion)
        self.materias.append(nueva_materia)
        return self.materias    
    def asignar_materia_nota_alumno(self, Alumno, nombre_materia, resolucion, nota):
        materia = Materias(nombre_materia, resolucion)
        Alumno.agregar_materia_nota(materia, nota) #Traigo de la clase alumno el metodo agregar materia.
   
    def get_materias(self):
        return [str(materia) for materia in self.materias]
   
class Materias:
    def __init__(self, nombre, resolucion):
        self.nombre = nombre
        self.resolucion = resolucion
        self.lista_materias = []

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_resolucion(self):
        return self.resolucion

    def set_resolucion(self, value):
        self.resolucion = value
   
    def agregar_materias(self, nombre, resolucion):
        materia = Materias(nombre, resolucion, nombre)
        self.lista_materias.append(materia)
        return self.lista_materias

    def __str__(self):
        return f"{self.nombre} Resolución: {self.resolucion}"

   


profesor1 = Profesor("Raul", "Portales", 74, 7895642, "2325287415", []) #creo un profesor
profesor1.asignar_materias("Matematica", "5847/17") # Le asigno una materia

print(profesor1.get_materias()) #obtengo las materias de un profesor
print(profesor1)

profesor1.asignar_materias("Pedagogia", "5599/14") #Asigno materias a un profesor
print(profesor1.get_materias())

alumno1 = Alumno("Ana", "Gomez", 20, 12345678, "A001") #Creo un objeto de la clase alumno

profesor1.asignar_materia_nota_alumno(alumno1, "Matemática", "5847/17", 8.5) #Asigno una materia y nota al alumno

print("Materias y notas del alumno:")
print(alumno1.consultar_materias_notas())# a través de alumno consulto la asignación

