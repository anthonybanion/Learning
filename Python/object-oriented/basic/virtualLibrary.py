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
#Version: 1.0

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Clase base abstracta
class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar_informacion(self):
        pass

# Clases derivadas de Persona
class Autor(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.lista_libros = []

    def mostrar_informacion(self):
        return f'Autor: {self.nombre}'

    def escribir_libro(self, libro):
        self.lista_libros.append(libro)

class Usuario(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre)
        self.email = email
        self.lista_libros_prestados = []

    def mostrar_informacion(self):
        return f'Usuario: {self.nombre}, Email: {self.email}'

    def prestar_libro(self, libro):
        self.lista_libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.lista_libros_prestados:
            self.lista_libros_prestados.remove(libro)

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.prestado = False

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f'{self.titulo} - {self.autor} - {self.numero_paginas} páginas - {estado}'

    def marcar_prestado(self):
        self.prestado = True

    def marcar_devuelto(self):
        self.prestado = False

# Clase Prestamo
class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_informacion(self):
        return (f'Préstamo del libro "{self.libro.titulo}" a {self.usuario.nombre}. '
                f'Fecha de préstamo: {self.fecha_prestamo.strftime("%Y-%m-%d")}, '
                f'Fecha de devolución: {self.fecha_devolucion.strftime("%Y-%m-%d")}.')

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, titulo):
        return [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]

    def buscar_usuario(self, nombre):
        return [usuario for usuario in self.usuarios if nombre.lower() in usuario.nombre.lower()]

    def realizar_prestamo(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        if libro not in self.libros:
            return "Libro no encontrado en la biblioteca."
        if libro.prestado:
            return "Libro ya está prestado."
        libro.marcar_prestado()
        usuario.prestar_libro(libro)
        prestamo = Prestamo(usuario, libro, fecha_prestamo, fecha_devolucion)
        self.prestamos.append(prestamo)
        return "Préstamo realizado con éxito."

    def devolver_libro(self, usuario, libro):
        for prestamo in self.prestamos:
            if prestamo.libro == libro and prestamo.usuario == usuario:
                libro.marcar_devuelto()
                usuario.devolver_libro(libro)
                self.prestamos.remove(prestamo)
                return "Libro devuelto con éxito."
        return "Préstamo no encontrado."

# Ejemplo de uso
if __name__ == "__main__":
    # Crear biblioteca
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 96)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)

    # Registrar libros
    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)

    # Crear usuario
    usuario1 = Usuario("Juan Pérez", "juan.perez@example.com")

    # Registrar usuario
    biblioteca.registrar_usuario(usuario1)

    # Realizar préstamo
    fecha_hoy = datetime.now()
    fecha_devolucion = fecha_hoy + timedelta(days=7)
    resultado_prestamo = biblioteca.realizar_prestamo(usuario1, libro1, fecha_hoy, fecha_devolucion)
    print(resultado_prestamo)

    # Mostrar libros en la biblioteca
    for libro in biblioteca.libros:
        print(libro)

    # Mostrar préstamos
    for prestamo in biblioteca.prestamos:
        print(prestamo.mostrar_informacion())

    # Devolver libro
    resultado_devolucion = biblioteca.devolver_libro(usuario1, libro1)
    print(resultado_devolucion)

    # Mostrar estado actualizado de los libros
    for libro in biblioteca.libros:
        print(libro)
