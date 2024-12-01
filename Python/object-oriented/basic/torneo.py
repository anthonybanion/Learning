#Brief: Crear un programa que permita crear equipos de futbol y agregarlos a un torneo
#Date: 13/11/2024
#Version: 1.0

class Equipo:
    def __init__(self, nombre, ciudad, jugadores):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__jugadores = jugadores
    
    def __str__(self):
        return f"Equipo: {self.__nombre} - Ciudad: {self.__ciudad} - Jugador: {self.__jugadores}"
    
    def mostrar_detalles(self):
        return f"Equipo: {self.__nombre}\n-Ciudad: {self.__ciudad}\n-Jugador: {self.__jugadores}"
    


class Torneo:
    def __init__(self, nombre_torneo):
        self.__nombre_torneo = nombre_torneo
        self.__equipos = []
    
    def __str__(self):
        return f"Torneo: {self.__nombre_torneo}"
    
    def agregar_equipo(self, equipo):
        self.__equipos.append(equipo)
    
    def mostrar_equipos(self):
        for equipo in self.__equipos:
            print(equipo)



def listar_equipos():
    equipos = []
    equipos.append(Equipo("River", "Buenos Aires", ["Enzo Perez", "Rafael Santos Borre", "Matias Suarez"]))
    equipos.append(Equipo("Boca", "Buenos Aires", ["Carlos Tevez", "Mauro Zarate", "Franco Soldano"]))
    return equipos





# jugadoresRiver = ["Enzo Perez", "Rafael Santos Borre", "Matias Suarez"]
# river = Equipo("River", "Buenos Aires", jugadoresRiver)
# jugadoresBoca = ["Carlos Tevez", "Mauro Zarate", "Franco Soldano"]
# boca = Equipo("Boca", "Buenos Aires", jugadoresBoca)

# print(river.mostrar_detalles())
# print(boca.mostrar_detalles())

# primeraDivision = Torneo("Primera Division")
# primeraDivision.agregar_equipo(river)
# primeraDivision.agregar_equipo(boca)

# primeraDivision.mostrar_equipos()