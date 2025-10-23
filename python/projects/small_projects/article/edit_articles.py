#Brief: Edit data manually
#Description: This file contains the function to edit data manually from the database.
#Date: 05/11/2024
#Author: Wilchez
#version: 1.0

from connection import DBConn
import sqlite3

# Conectar a la base de datos
db_manager = DBConn("sqlite/db_test.sqlite3")
db_manager.connect()

# Función para editar los campos de un artículo seleccionado
def edit_article():
    try:
        while True:
            # Solicitar al usuario que ingrese el criterio de búsqueda (código, descripción o ID)
            search_criteria = input("Por favor ingrese el criterio de búsqueda (código, descripción o ID): ").strip().lower()

            # Solicitar al usuario que ingrese el valor del criterio de búsqueda
            search_value = input(f"Por favor ingrese el valor del {search_criteria}: ").strip()

            # Verificar si el criterio de búsqueda es válido
            if search_criteria not in ['codigo', 'descripcion', 'id']:
                print("El criterio de búsqueda ingresado no es válido.")
                continue

            # Realizar la búsqueda en la tabla articulos
            db_manager.cursor.execute(f"SELECT * FROM articulos WHERE {search_criteria} = ?", (search_value,))
            article = db_manager.cursor.fetchone()

            # Verificar si se encontró el artículo
            if article:
                print("Artículo encontrado:")
                print(article)

                # Solicitar al usuario que ingrese los nuevos valores para los campos
                new_codigo = input("Nuevo código (deje vacío para mantener el mismo): ").strip() or article[1]
                new_nombre = input("Nuevo nombre (deje vacío para mantener el mismo): ").strip() or article[2]
                new_stock = input("Nuevo stock (deje vacío para mantener el mismo): ").strip() or article[3]
                new_detalle = input("Nuevo detalle (deje vacío para mantener el mismo): ").strip() or article[4]

                # Actualizar los campos del artículo
                db_manager.cursor.execute(
                    "UPDATE articulos SET codigo = ?, nombre = ?, stock = ?, detalle = ? WHERE id = ?",
                    (new_codigo, new_nombre, new_stock, new_detalle, article[0])
                )

                # Confirmar la transacción
                db_manager.connection.commit()
                print("Datos del artículo actualizados con éxito.")
            else:
                print("No se encontró ningún artículo con el criterio de búsqueda especificado.")

            # Preguntar si desea editar otro artículo
            another = input("¿Desea editar otro artículo? (s/n): ").strip().lower()
            if another != 's':
                break  # El break está dentro del bucle, ahora es correcto

    except sqlite3.Error as e:
        print(f"Error al editar datos: {e}")

# Llamar a la función para editar los campos de un artículo
edit_article()

# Verificar los datos en la tabla articulos
db_manager.cursor.execute("SELECT * FROM articulos")
table = db_manager.cursor.fetchall()
for row in table:
    print(row)

# Cerrar la conexión
db_manager.close()