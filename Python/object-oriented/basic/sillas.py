#Brief: Create a class called sillas
#Date: 05/11/2024
#Version: 1.0

class sillas:
    def __init__(self, nombre, color, madera):
        self.nombre = nombre
        self.color = color
        self.madera = madera
    
    def __str__(self):
        return f"{self.nombre} {self.color} {self.madera}"

sillas1=sillas("Silla1", "Blanca", "Pino")

print(sillas1)
    