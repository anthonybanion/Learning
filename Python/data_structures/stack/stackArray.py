# Clase que representa una pila (stack) implementada con un array (lista)
class Pila:
    def __init__(self):
        # Inicializamos la pila como una lista vacía
        self.pila = []

    # Método para agregar un elemento a la pila (Push)
    def agregar(self, elemento):
        self.pila.append(elemento)  # Agregamos el elemento al final de la lista

    # Método para eliminar el último elemento de la pila (Pop manual)
    def eliminar(self):
        if not self.esta_vacia():
            # Guardamos el último elemento y lo eliminamos manualmente
            elemento = self.pila[-1]
            self.pila = self.pila[:-1]
            return elemento
        else:
            return "La pila está vacía"

    # Método para obtener el último elemento de la pila sin eliminarlo (Peek)
    def obtener_ultimo(self):
        if not self.esta_vacia():
            return self.pila[-1]
        else:
            return "La pila está vacía"

    # Método para verificar si la pila está vacía
    def esta_vacia(self):
        return len(self.pila) == 0

    # Método para ordenar la pila en orden ascendente
    def ordenar(self):
        self.pila.sort()

    # Método para mostrar todos los elementos de la pila
    def mostrar(self):
        if not self.esta_vacia():
            return self.pila
        else:
            return "La pila está vacía"


# Ejemplo de uso de la clase Pila
if __name__ == "__main__":
    # Creamos una instancia de la pila
    mi_pila = Pila()

    # Agregamos elementos a la pila
    mi_pila.agregar(5)
    mi_pila.agregar(3)
    mi_pila.agregar(8)
    mi_pila.agregar(1)

    # Mostramos la pila
    print("Pila actual:", mi_pila.mostrar())

    # Eliminamos el último elemento
    print("Elemento eliminado:", mi_pila.eliminar())

    # Mostramos la pila después de eliminar un elemento
    print("Pila después de eliminar:", mi_pila.mostrar())

    # Ordenamos la pila
    mi_pila.ordenar()
    print("Pila ordenada:", mi_pila.mostrar())

    # Obtenemos el último elemento sin eliminarlo
    print("Último elemento:", mi_pila.obtener_ultimo())

    # Verificamos si la pila está vacía
    print("¿La pila está vacía?", mi_pila.esta_vacia())