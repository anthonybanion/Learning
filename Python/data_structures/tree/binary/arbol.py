import graphviz 

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        """Agrega un nodo al árbol siguiendo las reglas de un ABB"""
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._agregar(self.raiz, dato)

    def _agregar(self, nodo, dato):
        # if dato < nodo.dato:  # va a la izquierda
        if nodo.izquierdo is None:
            nodo.izquierdo = Nodo(dato)
        elif nodo.derecho is None:
            nodo.derecho = Nodo(dato)
        else:  
            if nodo.izquierdo.izquierdo is None or nodo.izquierdo.derecho is None:
                self._agregar(nodo.izquierdo, dato)
            else:
                self._agregar(nodo.derecho, dato)

    def completarNivel(self):
        """Completa el árbol hasta el nivel completo"""
        if self.raiz is None:
            return
        self._completar_nivel(self.raiz)

    def _completar_nivel(self, nodo):
        """Completa el árbol hasta el nivel completo de manera recursiva"""
        if nodo.izquierdo is None and nodo.derecho is None:
            nodo.izquierdo = Nodo(None)
            nodo.derecho = Nodo(None)
        if nodo.izquierdo:
            self._completar_nivel(nodo.izquierdo)
        if nodo.derecho:
            self._completar_nivel(nodo.derecho)

    def imprimir(self, nodo=None, nivel=0, prefijo="raíz: "):
        """Imprime el árbol de manera recursiva"""
        if nodo is None:
            nodo = self.raiz
        print(" " * nivel + prefijo + str(nodo.dato))
        if nodo.izquierdo:
            self.imprimir(nodo.izquierdo, nivel + 2, "izq → ")
        if nodo.derecho:
            self.imprimir(nodo.derecho, nivel + 2, "der → ")



    
    def graficar_arbol(self):
        """Dibuja el árbol binario usando Graphviz"""
        dot = graphviz.Digraph(comment="Árbol Binario")
        self._graficar_arbol(self.raiz, dot)
        dot.render("arbol_binario", format="png", view=True)  # crea y abre PNG

    def _graficar_arbol(self, nodo, dot):
        if nodo is not None:
            dot.node(str(nodo.dato), str(nodo.dato))  # crea el nodo

            if nodo.izquierdo is not None:
                dot.edge(str(nodo.dato), str(nodo.izquierdo.dato))
                self._graficar_arbol(nodo.izquierdo, dot)

            if nodo.derecho is not None:
                dot.edge(str(nodo.dato), str(nodo.derecho.dato))
                self._graficar_arbol(nodo.derecho, dot)





if __name__ == "__main__":
    # Example usage

    arbol = Arbol()

    arbol.agregar(0)
    arbol.agregar(1)
    arbol.agregar(2)
    arbol.agregar(3)
    arbol.agregar(4)
    arbol.agregar(5)
    arbol.agregar(6)
    arbol.agregar(7)
    arbol.agregar(8)
    arbol.agregar(9)
    arbol.agregar(10)
    arbol.agregar(11) 
    arbol.agregar(12)
    arbol.agregar(13)
    arbol.agregar(14)
    arbol.agregar(15) 
    arbol.agregar(16)
    arbol.agregar(17)
    arbol.agregar(18)
    arbol.agregar(19)
    arbol.agregar(20)
    arbol.agregar(21)
    arbol.agregar(22)
    arbol.agregar(23)
    arbol.agregar(24)
    arbol.agregar(25)
    arbol.agregar(26)
    arbol.agregar(27)
    arbol.agregar(28)
    arbol.agregar(29) 
    arbol.agregar(30)
    arbol.agregar(31)
    arbol.agregar(32)
    arbol.agregar(33) 
    arbol.agregar(34)
    arbol.agregar(35)        
    arbol.imprimir()

    arbol.graficar_arbol()
    

 
