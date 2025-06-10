#Brief: Course
#Detail: The relationship between the two classes is many-to-many, where each student can be in many courses and a course has many students.
#Date: 06/11/2024
#Version: 1.0

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []  # Lista de cursos

    def agregar_curso(self, curso):
        self.cursos.append(curso)

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []  # Lista de estudiantes

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

# Relación muchos a muchos: un estudiante puede estar en muchos cursos y un curso tiene muchos estudiantes
curso_python = Curso("Python Avanzado")
curso_java = Curso("Java Básico")

estudiante1 = Estudiante("Juan")
estudiante2 = Estudiante("Ana")

# Asociar estudiantes a los cursos
estudiante1.agregar_curso(curso_python)
estudiante1.agregar_curso(curso_java)
estudiante2.agregar_curso(curso_python)

curso_python.agregar_estudiante(estudiante1)
curso_python.agregar_estudiante(estudiante2)
curso_java.agregar_estudiante(estudiante1)

# Mostrar cursos de cada estudiante
for estudiante in [estudiante1, estudiante2]:
    print(f"{estudiante.nombre} está inscrito en los siguientes cursos:")
    for curso in estudiante.cursos:
        print(f"  - {curso.nombre}")

# Mostrar estudiantes de cada curso
for curso in [curso_python, curso_java]:
    print(f"El curso {curso.nombre} tiene los siguientes estudiantes:")
    for estudiante in curso.estudiantes:
        print(f"  - {estudiante.nombre}")
