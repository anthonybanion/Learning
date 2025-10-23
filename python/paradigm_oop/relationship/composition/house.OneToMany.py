#Brief: House
#Detail: The relationship between the two classes is one-to-many, where each house has many rooms.
#Date: 06/11/2024
#Version: 1.0


class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Habitación '{self.nombre}' creada.")

    def descripcion(self):
        print(f"Esta es la habitación {self.nombre}.")


class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        # Composición: La casa tiene varias habitaciones
        self.habitaciones = [
            Habitacion("Sala"),
            Habitacion("Cocina"),
            Habitacion("Dormitorio"),
        ]

    def mostrar_habitaciones(self):
        print(f"La casa en {self.direccion} tiene las siguientes habitaciones:")
        for habitacion in self.habitaciones:
            habitacion.descripcion()


# Creación de casa con habitaciones (uno a muchos)
mi_casa = Casa("Calle Ficticia 123")
mi_casa.mostrar_habitaciones()

# Si la casa se destruye, todas las habitaciones asociadas también lo serán.
