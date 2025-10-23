#Brief: Library
#Detail: The relationship between the two classes is many-to-many, where each book can be in many libraries.
#Date: 06/11/2024
#Version: 1.0


# Relación muchos a muchos usando agregación
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # Lista de libros

    def agregar_libro(self, libro):
        self.libros.append(libro)

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.bibliotecas = []  # Lista de bibliotecas

    def agregar_biblioteca(self, biblioteca):
        self.bibliotecas.append(biblioteca)

# Relación muchos a muchos: un libro puede estar en muchas bibliotecas
biblioteca1 = Biblioteca("Biblioteca Central")
biblioteca2 = Biblioteca("Biblioteca del Barrio")

libro1 = Libro("Python para todos")
libro2 = Libro("Java en 24 horas")

# Agregar libros a las bibliotecas
biblioteca1.agregar_libro(libro1)
biblioteca2.agregar_libro(libro1)
biblioteca2.agregar_libro(libro2)

# Agregar bibliotecas a los libros
libro1.agregar_biblioteca(biblioteca1)
libro1.agregar_biblioteca(biblioteca2)
libro2.agregar_biblioteca(biblioteca2)

# Mostrar bibliotecas de cada libro
for libro in [libro1, libro2]:
    print(f"El libro {libro.titulo} está en las siguientes bibliotecas:")
    for biblioteca in libro.bibliotecas:
        print(f"  - {biblioteca.nombre}")

# Mostrar libros de cada biblioteca
for biblioteca in [biblioteca1, biblioteca2]:
    print(f"La biblioteca {biblioteca.nombre} tiene los siguientes libros:")
    for libro in biblioteca.libros:
        print(f"  - {libro.titulo}")
