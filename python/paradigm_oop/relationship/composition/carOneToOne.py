#Brief: Car
#Detail: The relationship between the two classes is one-to-one, where each car has a unique motor.
#Date: 06/11/2024
#Version: 1.0


class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        print(f"Motor {self.tipo} creado.")

    def arrancar(self):
        print(f"El motor {self.tipo} está arrancando.")


class Coche:
    def __init__(self, marca, tipo_motor):
        self.marca = marca
        # Composición: El coche tiene un motor
        self.motor = Motor(tipo_motor)

    def encender(self):
        print(f"Encendiendo el coche {self.marca}...")
        self.motor.arrancar()


# Creación del coche y motor (uno a uno)
coche1 = Coche("Ferrari", "V8")
coche1.encender()

# El motor no puede existir sin el coche.
# Si coche1 se destruye, el motor asociado también se destruye.
