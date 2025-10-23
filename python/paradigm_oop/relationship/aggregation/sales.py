#brief: Ejemplo de relación de agregación entre clases
#detail: En este ejemplo, se muestra cómo se puede implementar una relación de agregación entre dos clases en Python.
#date: 12/11/2024
#version: 1.0

#from abc import ABC, abstractmethod

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.__stock = stock

    def __str__(self):
        return f'{self.nombre} - {self.precio} - {self.__stock}'
    
    def agregar_stock(self, cantidad):
        self.__stock += cantidad
    
    def ver_stock(self):
        return self.__stock

    def descrementar_stock(self, cantidad):
        if self.__stock >= cantidad:
            self.__stock -= cantidad
            return cantidad * self.precio
        return 0


class Ventas:
    def __init__(self):
        self.lista_producto = []  # Lista de productos vendidos
    
    
    def agregar_producto(self, producto, cantidad):
        self.lista_producto.append((producto, cantidad))
    
    def total_venta(self):
        total = 0
        for producto, cantidad in self.lista_producto:
            total += producto.descrementar_stock(cantidad)
        return total
    
    def __str__(self):
        return f'{self.lista_producto}'


class Factura:
    def __init__(self, ventas, fecha):
       self.ventas = ventas
       self.fecha = fecha
    
    def total_factura(self):
        return self.ventas.total_venta()
    
    def __str__(self):
        return f' {self.fecha}'


# Crear productos
producto1 = Producto("Camiseta", 25.5, 100)
producto2 = Producto("Pantalón", 40.0, 50)
# Agregar stock al producto 1
producto1.agregar_stock(10)
print(producto1.ver_stock())
# Crear una venta
venta1 = Ventas()

# Agregar productos a la venta
venta1.agregar_producto(producto1, 2)  # 2 camisetas
venta1.agregar_producto(producto2, 1)  # 1 pantalón

# Ver el total de la venta
print(f"Total de la venta: ${venta1.total_venta()}")

# Crear una factura para la venta
factura1 = Factura(venta1, "2024-11-12")
print(factura1.total_factura())
# Ver los detalles de la factura
print(factura1)


