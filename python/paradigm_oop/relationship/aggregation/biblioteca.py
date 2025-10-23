class Libro:
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} por {self.autor}, Año: {self.ano}, Género: {self.genero}"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_por_genero(self, genero):
        encontrados = [libro for libro in self.libros if libro.genero.lower() == genero.lower()]
        return encontrados

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                self.libros.remove(libro)
                print(f"Libro '{titulo}' eliminado de la biblioteca.")
                return
        print(f"Libro '{titulo}' no encontrado en la biblioteca.")

    def mostrar_libros(self):
        if self.libros:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(libro)
        else:
            print("No hay libros en la biblioteca.")







libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 1967, "Novela")
libro2 = Libro("Harry Potter y la piedra filosofal", "JkRowling", 1997, "Fantástico")

#Llamo a biblioteca, lo asigno a variable para que no me de error, que falta el argumento self.
biblioteca = Biblioteca()

#Agrego los libros creados mas arriba a la biblioteca.
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

#Muestro libros de la biblioteca
biblioteca.mostrar_libros()

# Buscar libros por género
print("\nLibros de género 'Novela':")
for libro in biblioteca.buscar_por_genero("Novela"):#Hace un like de Novela, tiene que ser igual a
                                                    #lo que se hizo en la creacion del libro
    print(libro)

# Eliminar un libro
biblioteca.eliminar_libro("Cien años de soledad")#Lo mismo, elimina por nombre exacto.

# Mostrar libros después de la eliminación
biblioteca.mostrar_libros()