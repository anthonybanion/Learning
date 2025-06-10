#Brief:
#   Defina una clase libro con atributos como titulo, autor y isbn
#   Defina la clase biblioteca que tenga atributo nombre y una lista de libros
#   Implemente metodos en la biblioteca para
#   -Agregar libros a la coleccion
#   -Mostrar la lista de libros disponible
#   -Crear instancia de Libros y agregarlas a una instancia de biblioteca
#Date: 13/11/2024
#Version: 1.0


class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
    
    def __str__(self):
        return f"Libro: {self.__titulo} - Autor: {self.__autor} - ISBN: {self.__isbn}"
    
    def mostrar_detalles(self):
        return f"Libro: {self.__titulo}\n-Autor: {self.__autor}\n-ISBN: {self.__isbn}"
    
class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []
    
    def __str__(self):
        return f"Biblioteca: {self.__nombre}"
    
    def agregar_libro(self, libro):
        self.__libros.append(libro)
    
    def mostrar_libros(self):
        for libro in self.__libros:
            print(libro)

libro1 = Libro("El principito", "Antoine de Saint-Exupery", "978-987-612-000-0")
libro2 = Libro("El tunel", "Ernesto Sabato", "978-950-731-731-0")
libro3 = Libro("El amor en los tiempos del colera", "Gabriel Garcia Marquez", "978-950-731-731-0")

biblioteca = Biblioteca("Biblioteca Nacional")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

biblioteca.mostrar_libros()