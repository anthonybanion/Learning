#Brief: Course
#Detail: The relationship between the two classes is one-to-many, where each course has many students.
#Date: 06/11/2024
#Version: 1.0


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []  # Lista de estudiantes

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

# Relación 1 a muchos: un curso tiene muchos estudiantes
curso_python = Curso("Python Avanzado")
estudiante1 = Estudiante("Juan")
estudiante2 = Estudiante("Ana")

curso_python.agregar_estudiante(estudiante1)
curso_python.agregar_estudiante(estudiante2)

for estudiante in curso_python.estudiantes:
    print(f"{estudiante.nombre} está inscrito en el curso {curso_python.nombre}")
