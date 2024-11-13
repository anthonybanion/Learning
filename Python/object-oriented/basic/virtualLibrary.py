# Sistema de gestión de una Biblioteca Digital
# Objetos: Libro, Autor, Usuario, Prestamo.
# Conceptos aplicados: 
# - Herencia: Persona -> Autor, Usuario
# - Polimorfismo: método `mostrar_informacion()` sobrecargado
# - Abstracción: clases abstractas (Persona, ElementoBibliografico)
# - Relaciones: 
#   - Composición: Autor -> Libro
#   - Agregación: Usuario -> Libro prestado
#   - Asociación: Prestamo -> Usuario, Libro
# Métodos: registro, préstamo, devolución, búsqueda de libros y usuarios.

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar_informacion(self):
        pass

class Autor(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.lista_libros = [
            Libro('El principito', 'Antoine de Saint-Exupéry', 100),
            Libro('Cien años de soledad', 'Gabriel García Márquez', 200),
            Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 300),
            Libro('La Odisea', 'Homero', 400),
            Libro('La Iliada', 'Homero', 500),
            Libro('La Divina Comedia', 'Dante Alighieri', 600),
            Libro('Hamlet', 'William Shakespeare', 700),
            Libro('El retrato de Dorian Gray', 'Oscar Wilde', 800),
            Libro('La metamorfosis', 'Franz Kafka', 900),
        ]
    
    def mostrar_informacion(self):
        return f'Autor: {self.nombre}'
    
    def escribir_libro(self, libro):
        self.lista_libros.append(libro)

class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas

    def __str__(self):
        return f'{self.titulo} - {self.autor} - {self.numero_paginas}'
    
class Usuario(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre)
        self.email = email
        self.lista_libros_prestados = []

    def mostrar_informacion(self):
        return f'Usuario: {self.nombre}'
    
    def prestar_libro(self, libro):
        self.lista_libros_prestados.append(libro)

class Prestamo:
    def __init__(self, fecha_devolucion, libro, fecha_prestamo):
        self.fecha_devolucion = fecha_devolucion
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo

    def __str__(self):
        return f'{self.fecha_devolucion} - {self.libro} - {self.fecha_prestamo}'