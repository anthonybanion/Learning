import graphviz 

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.nodo_derecho = None
        self.nodo_izquierdo = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def agregarNodo(self, dato):
        new_node = Nodo(dato)
        if self.raiz is None:
            self.raiz = new_node
        else:
            self.agregarHijo(self.raiz, dato)

    def agregarHijo(self, dato):
        if self.nodo_izquierdo is None:
            self.nodo_izquierdo = Nodo(dato)
        else:
            self.agregarHijo(self.nodo_izquierdo, dato)
        if self.nodo_derecho is None:
            self.nodo_izquierdo = Nodo(dato)
        else:
            self.agregarHijo(self.nodo_derecho, dato)

    def mostrarArbol(self):
        actual = self.raiz
        while actual:
            print(actual.dato)

        print("None")

    def graficar_arbol(self):
        dot = graphviz.Diagraph(comment='Arbol Binario')
        self._graficar_arbol(self.rai, dot)
        dot.render('arbol_binario', view=True)

        def _graficar_arbol(slef, nodo, dot):
            if nodo is not None:
                dot.node(str(nodo.valor), str(nodo.valor))
                if nodo.izquierdo is not None:
                    dot.edge(str(nodo.valor), str(nodo.izquierdo.valor))
        self._graficar_arbol()





if __name__ == "__main__":
    # Example usage

    arbol = Arbol()

    arbol.agregarNodo('raiz')
    arbol.agregarNodo('A')
 
