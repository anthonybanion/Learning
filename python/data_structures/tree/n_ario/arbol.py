

# class Nodo():
#     def __init__(self, dato):
#         self.dato = dato
#         self.hijos=[]

#     def agregarHijo(self,nodo):
#         self.hijos.append(nodo)
       
#     def mostrar(self, nivel=0):
#         print("  " * nivel + str(self.dato))
#         for hijo in self.hijos:
#             hijo.mostrar(nivel + 1)
           
#     def contar_nodos(self):
#         total = 1
#         for hijo in self.hijos:
#             total += hijo.contar_nodos()
#         return total

#     def altura(self):
#         if not self.hijos:
#             return 1
#         return 1 + max(hijo.altura() for hijo in self.hijos)

#     def buscar(self, dato):
#         if self.dato == dato:
#             return self
#         for hijo in self.hijos:
#             encontrado = hijo.buscar(dato)
#             if encontrado:
#                 return encontrado
#         return None

#     def mostrar_hojas(self):
#         if not self.hijos:
#             print(self.dato)
#             return 1
#         total = 0
#         for hijo in self.hijos:
#             total += hijo.mostrar_hojas()
#         return total

# print("#############Mostrando###########")            
# raiz = Nodo("Animal")
# print("\n")


# vertebrado = Nodo("Vertebrado")
# invertebrado = Nodo("Invertebrado")

# ave = Nodo("Ave")
# insecto = Nodo("Insecto")

# raiz.agregarHijo(vertebrado)
# raiz.agregarHijo(invertebrado)

# vertebrado.agregarHijo(ave)
# invertebrado.agregarHijo(insecto)

# raiz.mostrar()

# print(f"Cantidad de nodos: {vertebrado.contar_nodos()}")
# print(f"Altura del árbol: {raiz.altura()}")

# busqueda = raiz.buscar("Ave")

# if busqueda:
#     print(f"{busqueda.dato}: Encontrado")
# else:
#     print(f"No se encontró el valor: {busqueda.dato}")

# print("Buscando hojas")  
# print(f"La cantidad de hojas es: {raiz.mostrar_hojas()}")

#En clase separando responsabilidades

from graphviz import Digraph

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

    def __str__(self):
        return f"Nodo({self.dato})"
   
class Arbol:
    def __init__(self):
        self.raiz = None

    def crear_raiz(self, dato):
        if self.raiz is not None:
            raise Exception("La raíz ya fue creada.")
        self.raiz = Nodo(dato)

    def obtener_raiz(self):
        return self.raiz

    def mostrar(self, nodo=None, nivel=0):
        if self.raiz is None:
            print("Árbol vacío.")
            return

        if nodo is None:
            nodo = self.raiz

        print("  " * nivel + f"- {nodo.dato}")
        for hijo in nodo.hijos:
            self.mostrar(hijo, nivel + 1)
       
    def graficar(self, nombre_archivo="arbol"):
        dot = Digraph()
        def agregar_nodos(nodo):
            dot.node(str(id(nodo)), nodo.dato)
            for hijo in nodo.hijos:
                dot.edge(str(id(nodo)), str(id(hijo)))
                agregar_nodos(hijo)
        if self.raiz:
            agregar_nodos(self.raiz)
        dot.render(nombre_archivo, format="png", cleanup=True)
        print(f"Árbol guardado como {nombre_archivo}.png")
       
arbol = Arbol()

arbol.crear_raiz("Raiz")

raiz = arbol.obtener_raiz()

elemento1= Nodo("elemento1")

elemento2= Nodo("elemento2")

elemento3 = Nodo("elemento3")

raiz.agregar_hijo(elemento1)

elemento1.agregar_hijo(elemento2)

elemento2.agregar_hijo(elemento3)
arbol.mostrar()

arbol.graficar("mi_arbol")