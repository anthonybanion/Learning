import sqlite3

#Conectar a la base de datos
conn = sqlite3.connect('./tienda.db')
cursor = conn.cursor()

#Crear la tabla producto si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS producto (
        ID INTEGER PRIMARY KEY,
        Nombre TEXT,
        Precio REAL,
        Cantidad INTEGER,
        Descripcion TEXT,
        Categoria TEXT
    )
''')

#Funciones del programa
def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    descripcion = input("Ingrese la descripción del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    
    cursor.execute('INSERT INTO producto (Nombre, Precio, Cantidad, Descripcion, Categoria) VALUES (?, ?, ?, ?, ?)', (nombre, precio, cantidad, descripcion, categoria))
    conn.commit()
    print(f"Producto {nombre} registrado con éxito.")

def mostrar_productos():
    cursor.execute('SELECT * FROM producto')
    productos = cursor.fetchall()
    for producto in productos:
        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Precio: {producto[2]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Descripción: {producto[4]}")
        print(f"Categoría: {producto[5]}")
        print("--------------------")

def actualizar_producto():
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    cursor.execute('SELECT * FROM producto WHERE ID = ?', (id_producto,))
    producto = cursor.fetchone()
    if producto:
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        cursor.execute('UPDATE producto SET Cantidad = ? WHERE ID = ?', (cantidad, id_producto))
        conn.commit()
        print(f"Producto {id_producto} actualizado con éxito.")
    else:
        print(f"No se encontró el producto con ID {id_producto}.")

def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    cursor.execute('SELECT * FROM producto WHERE ID = ?', (id_producto,))
    producto = cursor.fetchone()
    if producto:
        cursor.execute('DELETE FROM producto WHERE ID = ?', (id_producto,))
        conn.commit()
        print(f"Producto {id_producto} eliminado con éxito.")
    else:
        print(f"No se encontró el producto con ID {id_producto}.")

def buscar_producto():
    id_producto = int(input("Ingrese el ID del producto a buscar: "))
    cursor.execute('SELECT * FROM producto WHERE ID = ?', (id_producto,))
    producto = cursor.fetchone()
    if producto:
        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Precio: {producto[2]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Descripción: {producto[4]}")
        print(f"Categoría: {producto[5]}")
    else:
        print(f"No se encontró el producto con ID {id_producto}.")

def reporte_bajo_stock():
    limite = int(input("Ingrese el límite de stock: "))
    cursor.execute('SELECT * FROM producto WHERE Cantidad <= ?', (limite,))
    productos = cursor.fetchall()
    print("Productos con stock bajo:")
    for producto in productos:
        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Cantidad: {producto[3]}")

def main():
    while True:
        print("Menú de la tienda:")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de stock bajo")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "0":
            print("Gracias por utilizar el programa.")
            break
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    main()
    conn.close()


