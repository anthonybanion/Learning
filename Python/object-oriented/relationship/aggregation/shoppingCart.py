class Producto:
    def __init__(self, nombre, precio, stock):
      self.nombre = nombre
      self.precio = precio
      self.stock = stock
     
   
    def stock_disponible(self, cantidad):
        return self.stock >= cantidad
   
    def actualizar_stock(self, cantidad):
        self.stock -= cantidad
        if self.stock < 0:
            self.stock = 0
            print("No hay stock suficiente para realizar la compra.")
           
    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"
   

class ItemCarrito:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
   
    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} - Cantidad: {self.cantidad}, Subtotal: ${self.subtotal()}"

class Carrito:
    def __init__(self):
        self.items = []
       
    def agregar_producto(self, producto, cantidad):
        if producto.stock_disponible(cantidad):
            item = ItemCarrito(producto, cantidad)
            self.items.append(item)
            print(f"{producto.nombre} agregado al carrito.")
        else:
            print("No se pudo agregar el producto al carrito.")

    def remover_producto(self, nombre_producto):
        for item in self.items:
            if item.producto.nombre == nombre_producto:
                self.items.remove(item)
                print(f"{nombre_producto} removido del carrito.")
                return
        print(f"{nombre_producto} no se encuentra en el carrito.")

    def calcular_total(self):
        total = sum(item.subtotal() for item in self.items)
        return total

    def mostrar_carrito(self):
        if not self.items:
            print("El carrito está vacío.")
            return
        print("Productos en el carrito:")
        for item in self.items:
            print(item)
        print(f"Total: ${self.calcular_total()}")


producto1 = Producto("Laptop", 1500, 10)
producto2 = Producto("Mouse", 50, 100)

carrito = Carrito()
carrito.agregar_producto(producto1, 1)
carrito.agregar_producto(producto2, 2)

carrito.calcular_total()
carrito.mostrar_carrito()
carrito.remover_producto("Mouse")
carrito.mostrar_carrito()
