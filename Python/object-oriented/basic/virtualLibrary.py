#Brief: Virtual Library Management System
#Date: 25/11/2021
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
#Version: 2.0

from abc import ABC, abstractmethod
from datetime import datetime, timedelta


# Clase base abstracta
class Persona(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    @abstractmethod
    def mostrar_informacion(self):
        pass

    # Getter para el nombre (acceso controlado)
    def get_nombre(self):
        return self.__nombre


# Clases derivadas de Persona
class Autor(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self._lista_libros = []  # Atributo protegido

    def mostrar_informacion(self):
        return f'Autor: {self.get_nombre()}'

    def escribir_libro(self, libro):
        self._lista_libros.append(libro)

    def obtener_libros(self):
        return self._lista_libros


class Usuario(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre)
        self._email = email  # Atributo protegido
        self._lista_libros_prestados = []  # Atributo protegido

    def mostrar_informacion(self):
        return f'Usuario: {self.get_nombre()}, Email: {self._email}'

    def prestar_libro(self, libro):
        self._lista_libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self._lista_libros_prestados:
            self._lista_libros_prestados.remove(libro)

    # Getter para la lista de libros prestados
    def obtener_libros_prestados(self):
        return self._lista_libros_prestados


# Clase Libro
class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.__titulo = titulo  # Atributo privado
        self.__autor = autor  # Atributo privado
        self.__numero_paginas = numero_paginas  # Atributo privado
        self.__prestado = False  # Atributo privado

    def __str__(self):
        estado = "Prestado" if self.__prestado else "Disponible"
        return f'{self.__titulo} - {self.__autor} - {self.__numero_paginas} páginas - {estado}'

    # Métodos privados para controlar el estado del libro
    def marcar_prestado(self):
        self.__prestado = True

    def marcar_devuelto(self):
        self.__prestado = False

    # Getters para los atributos privados
    def get_titulo(self):
        return self.__titulo

    def get_estado(self):
        return self.__prestado


# Clase Prestamo
class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        self._usuario = usuario  # Atributo protegido
        self._libro = libro  # Atributo protegido
        self.__fecha_prestamo = fecha_prestamo  # Atributo privado
        self.__fecha_devolucion = fecha_devolucion  # Atributo privado

    def mostrar_informacion(self):
        return (f'Préstamo del libro "{self._libro.get_titulo()}" a {self._usuario.get_nombre()}. '
                f'Fecha de préstamo: {self.__fecha_prestamo.strftime("%Y-%m-%d")}, '
                f'Fecha de devolución: {self.__fecha_devolucion.strftime("%Y-%m-%d")}.')


# Nueva clase para manejar el catálogo de libros
class CatalogoLibros:
    def __init__(self):
        self._libros = []

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def buscar_libro(self, titulo):
        return [libro for libro in self._libros if titulo.lower() in libro.get_titulo().lower()]

    def listar_libros(self):
        return "\n".join(str(libro) for libro in self._libros)


# Nueva clase para manejar usuarios
class GestorUsuarios:
    def __init__(self):
        self._usuarios = []

    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def buscar_usuario(self, nombre):
        return [usuario for usuario in self._usuarios if nombre.lower() in usuario.get_nombre().lower()]

    def listar_usuarios(self):
        return "\n".join(usuario.mostrar_informacion() for usuario in self._usuarios)


# Refactor de la clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.catalogo = CatalogoLibros()
        self.usuarios = GestorUsuarios()
        self._prestamos = []

    def registrar_libro(self, libro):
        self.catalogo.agregar_libro(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.agregar_usuario(usuario)

    def realizar_prestamo(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        if libro not in self.catalogo._libros:
            raise ValueError("Libro no encontrado en la biblioteca.")
        if libro.get_estado():
            raise ValueError("Libro ya está prestado.")
        libro.marcar_prestado()
        usuario.prestar_libro(libro)
        prestamo = Prestamo(usuario, libro, fecha_prestamo, fecha_devolucion)
        self._prestamos.append(prestamo)

    def devolver_libro(self, usuario, libro):
        for prestamo in self._prestamos:
            if prestamo._libro == libro and prestamo._usuario == usuario:
                libro.marcar_devuelto()
                usuario.devolver_libro(libro)
                self._prestamos.remove(prestamo)
                return
        raise ValueError("Préstamo no encontrado.")

    def mostrar_prestamos(self):
        return "\n".join(prestamo.mostrar_informacion() for prestamo in self._prestamos)


# Código principal
biblioteca = Biblioteca()

# Crear y registrar libros
biblioteca.registrar_libro(Libro("El principito", "Antoine de Saint-Exupéry", 96))
biblioteca.registrar_libro(Libro("Cien años de soledad", "Gabriel García Márquez", 417))

# Crear y registrar usuarios
usuario1 = Usuario("Juan Pérez", "juan.perez@example.com")
biblioteca.registrar_usuario(usuario1)

# Realizar préstamo
fecha_hoy = datetime.now()
fecha_devolucion = fecha_hoy + timedelta(days=7)
biblioteca.realizar_prestamo(usuario1, biblioteca.catalogo.buscar_libro("El principito")[0], fecha_hoy, fecha_devolucion)

# Mostrar información
print("Libros en la biblioteca:")
print(biblioteca.catalogo.listar_libros())

print("\nPréstamos realizados:")
print(biblioteca.mostrar_prestamos())

# Devolver libro
biblioteca.devolver_libro(usuario1, biblioteca.catalogo.buscar_libro("El principito")[0])

print("\nEstado actualizado de los libros:")
print(biblioteca.catalogo.listar_libros())
