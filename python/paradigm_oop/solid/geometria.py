#Brief: Geometría
#Date: 05/11/2024
#Version: 1.0


from abc import ABC, abstractmethod
import math

# Principio de Segregación de Interfaces (cada clase implementa solo lo que necesita)
# Clase abstracta Figura - Principio de Sustitución de Liskov
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Principio de Responsabilidad Única: Cada clase tiene una responsabilidad única (calcular área y perímetro)
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio