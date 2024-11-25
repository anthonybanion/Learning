from abc import ABC, abstractmethod

# Clase abstracta: Persona
class Persona(ABC):
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    @abstractmethod
    def mostrar_informacion(self):
        pass

# Clase Cliente (Herencia de Persona)
class Cliente(Persona):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self.historial_compras = []  # Lista de pedidos realizados

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre}, dni: {self.dni}"

    def agregar_pedido(self, pedido):
        self.historial_compras.append(pedido)

# Clase Empleado (Herencia de Persona)
class Empleado(Persona):
    def __init__(self, nombre, dni, puesto):
        super().__init__(nombre, dni)
        self.puesto = puesto
        self.ventas_realizadas = 0

    def mostrar_informacion(self):
        return f"Empleado: {self.nombre}, dni: {self.dni}, Puesto: {self.puesto}"

    def registrar_venta(self):
        self.ventas_realizadas += 1

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio  # Encapsulamiento
        self.__stock = stock  # Encapsulamiento

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio

    @property
    def stock(self):
        return self.__stock

    def reducir_stock(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
        else:
            raise ValueError("Stock insuficiente")

    def __str__(self):
        return f"{self.nombre}: ${self.__precio}, Stock: {self.__stock}"

# Clase Carrito (Composición)
class Carrito:
    def __init__(self):
        self.productos = []  # Lista de productos en el carrito

    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.productos.append((producto, cantidad))
        else:
            raise ValueError(f"No hay suficiente stock para {producto.nombre}")

    def calcular_total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.productos)

    def vaciar(self):
        self.productos.clear()

# Clase Pedido (Agregación)
class Pedido:
    def __init__(self, cliente, carrito):
        self.cliente = cliente
        self.productos = carrito.productos  # Agregación de productos
        self.total = carrito.calcular_total()

    def procesar_pedido(self):
        for producto, cantidad in self.productos:
            producto.reducir_stock(cantidad)

    def __str__(self):
        detalles = "\n".join([f"{producto.nombre} x{cantidad}" for producto, cantidad in self.productos])
        return f"Pedido de {self.cliente.nombre}:\n{detalles}\nTotal: ${self.total:.2f}"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("Laptop", 1500, 10)
    producto2 = Producto("Auriculares", 100, 50)
    producto3 = Producto("Mouse", 25, 100)

    # Crear cliente
    cliente1 = Cliente("Juan Pérez", "12345678")

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
