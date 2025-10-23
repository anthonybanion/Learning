#Brief: Passport
#Detail: The relationship between the two classes is one-to-one, where each person has a unique passport.
#Date: 06/11/2024
#Version: 1.0



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Pasaporte:
    def __init__(self, numero):
        self.numero = numero

# Relación 1 a 1: cada persona tiene un pasaporte único
persona1 = Persona("Juan")
pasaporte1 = Pasaporte("12345AB")

# Asociación: una persona tiene un pasaporte
persona1.pasaporte = pasaporte1

print(f"{persona1.nombre} tiene el pasaporte con número {persona1.pasaporte.numero}")
