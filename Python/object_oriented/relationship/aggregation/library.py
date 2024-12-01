#Brief: Aggregation in Python
#Date: 05/11/2024
#Version: 1.0

#clase contenida
class Libro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor=autor

    def __repr__(self):
        return f'El libro es {self.titulo} por {self.autor}'
    
#clase contenedora
class Biblioteca():
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.libros = None
    
    def MuestraBiblioteca(self):
        print(self.nombre)
        print(self.ciudad)

        if self.libros==None:
            print('No hay libros')
        else:
            print(self.libros)
    
    def AgregaLibro(self, libro):
        if isinstance(libro, Libro):  #isinstance() es una función que devuelve True si el objeto es una instancia de la clase
            self.libros=libro
        else:
            print('Coloca un libro')
    
    def __del__(self):
        print('Se elimino biblioteca')
        

#creamos un libro
libro1=Libro('The Reference', 'Nicosio')
#creamos la biblioteca
biblioteca1=Biblioteca('Biblioteca central', 'NyC')
biblioteca1.MuestraBiblioteca()
print('..........')
#hacemos la agregacion
biblioteca1.AgregaLibro(libro1)
biblioteca1.MuestraBiblioteca()