from abc import ABC, abstractmethod

# Clase abstracta: Persona
class Persona(ABC):
    def __init__(self, nombre, email):
        self._nombre = nombre  # Encapsulado
        self._email = email  # Encapsulado

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    @abstractmethod
    def mostrar_informacion(self):
        pass

# Clase Cliente (Herencia de Persona)
class Cliente(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self._historial_compras = []  # Encapsulado

    def mostrar_informacion(self):
        return f"Cliente: {self._nombre}, Email: {self._email}"

    def agregar_pedido(self, pedido):
        self._historial_compras.append(pedido)

    def get_historial_compras(self):
        return self._historial_compras

# Clase Empleado (Herencia de Persona)
class Empleado(Persona):
    def __init__(self, nombre, email, puesto):
        super().__init__(nombre, email)
        self._puesto = puesto  # Encapsulado
        self._ventas_realizadas = 0  # Encapsulado

    def mostrar_informacion(self):
        return f"Empleado: {self._nombre}, Email: {self._email}, Puesto: {self._puesto}"

    def registrar_venta(self):
        self._ventas_realizadas += 1

    def get_ventas_realizadas(self):
        return self._ventas_realizadas

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre  # Encapsulado
        self._precio = precio  # Encapsulado
        self._stock = stock  # Encapsulado

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo")

    def get_stock(self):
        return self._stock

    def reducir_stock(self, cantidad):
        if cantidad <= self._stock:
            self._stock -= cantidad
        else:
            raise ValueError("Stock insuficiente")

    def __str__(self):
        return f"{self._nombre}: ${self._precio}, Stock: {self._stock}"

# Clase Carrito (Composición)
class Carrito:
    def __init__(self):
        self._productos = []  # Encapsulado

    def agregar_producto(self, producto, cantidad):
        if producto.get_stock() >= cantidad:
            self._productos.append((producto, cantidad))
        else:
            raise ValueError(f"No hay suficiente stock para {producto.get_nombre()}")

    def calcular_total(self):
        return sum(producto.get_precio() * cantidad for producto, cantidad in self._productos)

    def vaciar(self):
        self._productos.clear()

    def get_productos(self):
        return self._productos

# Clase Pedido (Agregación)
class Pedido:
    def __init__(self, cliente, carrito):
        self._cliente = cliente  # Encapsulado
        self._productos = carrito.get_productos()  # Agregación de productos
        self._total = carrito.calcular_total()  # Encapsulado

    def procesar_pedido(self):
        for producto, cantidad in self._productos:
            producto.reducir_stock(cantidad)

    def __str__(self):
        detalles = "\n".join([f"{producto.get_nombre()} x{cantidad}" for producto, cantidad in self._productos])
        return f"Pedido de {self._cliente.get_nombre()}:\n{detalles}\nTotal: ${self._total:.2f}"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("Laptop", 1500, 10)
    producto2 = Producto("Auriculares", 100, 50)
    producto3 = Producto("Mouse", 25, 100)

    # Crear cliente
    cliente1 = Cliente("Juan Pérez", "juan@gmail.com")

    # Crear carrito
    carrito = Carrito()
    carrito.agregar_producto(producto1, 1)
    carrito.agregar_producto(producto2, 2)

    # Crear pedido
    pedido = Pedido(cliente1, carrito)
    pedido.procesar_pedido()
    cliente1.agregar_pedido(pedido)

    # Mostrar información del pedido
    print(pedido)

    # Crear empleado
    empleado = Empleado("Ana López", "ana@gmail.com", "Vendedora")
    empleado.registrar_venta()

    # Mostrar información de las personas
    print(cliente1.mostrar_informacion())
    print(empleado.mostrar_informacion())
