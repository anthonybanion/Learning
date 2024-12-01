#Brief: Sistema de Gestión de Biblioteca Digital
# Este sistema permite gestionar una biblioteca digital, 
# incluyendo el registro de libros, usuarios y el manejo de préstamos. 
# Los usuarios pueden tomar libros prestados por un tiempo determinado y 
# devolverlos. La biblioteca ofrece funciones para agregar libros, 
# listar los disponibles, registrar usuarios y mostrar los préstamos activos.
#Date: 25/11/2021
#Version: 2.0

from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Persona(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre  

    @abstractmethod
    def mostrar_informacion(self):
        pass

    def get_nombre(self):
        return self.__nombre


class Autor(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self._lista_libros = []  # Lista de libros escritos por el autor

    def mostrar_informacion(self):
        return f'Autor: {self.get_nombre()}'

    def escribir_libro(self, libro):
        self._lista_libros.append(libro)

    def obtener_libros(self):
        return self._lista_libros


class Usuario(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre)
        self._email = email  
        self._lista_libros_prestados = [] # Lista de libros prestados al usuario

    def mostrar_informacion(self):
        return f'Usuario: {self.get_nombre()}, Email: {self._email}'

    def prestar_libro(self, libro):
        self._lista_libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self._lista_libros_prestados:
            self._lista_libros_prestados.remove(libro)

    def obtener_libros_prestados(self):
        return self._lista_libros_prestados


class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.__titulo = titulo  
        self.__autor = autor  # Autor es ahora una instancia de la clase Autor
        self.__numero_paginas = numero_paginas  
        self.__prestado = False  

    def __str__(self):
        estado = "Prestado" if self.__prestado else "Disponible"
        return f'{self.__titulo} - {self.__autor.get_nombre()} - {self.__numero_paginas} páginas - {estado}'

    def marcar_prestado(self):
        self.__prestado = True

    def marcar_devuelto(self):
        self.__prestado = False

    def get_titulo(self):
        return self.__titulo

    def get_estado(self):
        return self.__prestado

    def get_autor(self):
        return self.__autor


class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        self._usuario = usuario  
        self._libro = libro  
        self.__fecha_prestamo = fecha_prestamo 
        self.__fecha_devolucion = fecha_devolucion  

    def mostrar_informacion(self):
        return (f'Préstamo del libro "{self._libro.get_titulo()}" a {self._usuario.get_nombre()}. '
                f'Fecha de préstamo: {self.__fecha_prestamo.strftime("%Y-%m-%d")}, '
                f'Fecha de devolución: {self.__fecha_devolucion.strftime("%Y-%m-%d")}.')


class CatalogoLibros:
    def __init__(self):
        self._libros = []

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def buscar_libro(self, titulo):
        return [libro for libro in self._libros if titulo.lower() in libro.get_titulo().lower()]

    def listar_libros(self):
        return "\n".join(str(libro) for libro in self._libros)


class GestorUsuarios:
    def __init__(self):
        self._usuarios = []

    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def buscar_usuario(self, nombre):
        return [usuario for usuario in self._usuarios if nombre.lower() in usuario.get_nombre().lower()]

    def listar_usuarios(self):
        return "\n".join(usuario.mostrar_informacion() for usuario in self._usuarios)


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

# Crear autores
autor1 = Autor("Antoine de Saint-Exupéry")
autor2 = Autor("Gabriel García Márquez")

# Crear libros y asignarles un autor
libro1 = Libro("El principito", autor1, 96)
libro2 = Libro("Cien años de soledad", autor2, 417)


# Asignar el libro a la lista de libros del autor correspondiente
autor1.escribir_libro(libro1)
autor2.escribir_libro(libro2)

# Crear y registrar libros en la biblioteca
biblioteca.registrar_libro(libro1)
biblioteca.registrar_libro(libro2)

# Crear y registrar usuarios
usuario1 = Usuario("Juan Pérez", "juan.perez@example.com")
usuario2 = Usuario("Mario", "mario@gmail.com")
biblioteca.registrar_usuario(usuario1)

# Realizar préstamo
fecha_hoy = datetime.now()
fecha_devolucion = fecha_hoy + timedelta(days=7)
biblioteca.realizar_prestamo(usuario1, biblioteca.catalogo.buscar_libro("El principito")[0], fecha_hoy, fecha_devolucion)
biblioteca.realizar_prestamo(usuario2, biblioteca.catalogo.buscar_libro("El principito")[0], fecha_hoy, fecha_devolucion)
# Mostrar información
print("Libros en la biblioteca:")
print(biblioteca.catalogo.listar_libros())

print("\nPréstamos realizados:")
print(biblioteca.mostrar_prestamos())
s
# Devolver libro
# biblioteca.devolver_libro(usuario1, biblioteca.catalogo.buscar_libro("El principito")[0])

print("\nEstado actualizado de los libros:")
print(biblioteca.catalogo.listar_libros())

# print(f"Libros de {autor1.get_nombre()}:")
# print([libro.get_titulo() for libro in autor1.obtener_libros()])
