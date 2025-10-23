#Brief: Insert data manually
#Description:  This file contains the function to insert data manually into the database.
#Date: 05/11/2024
#Author: Wilchez
#version: 1.0

from connection import DBConn
import sqlite3

db_manager = DBConn("sqlite/db_test.sqlite3")
db_manager.connect()

def insert_data_manually():
    try:
        # Solicitar al usuario que ingrese los datos
        while True:
            codigo = input("Por favor ingrese el código del artículo: ")
            nombre = input("Por favor ingrese el nombre del artículo: ")
            stock = int(input("Por favor ingrese el stock del artículo: "))
            detalle = input("Por favor ingrese el detalle del artículo: ")

            # Insertar los datos en la tabla
            db_manager.cursor.execute(
                "INSERT INTO articulos (codigo, nombre, stock, detalle) VALUES (?, ?, ?, ?)",
                (codigo, nombre, stock, detalle)
            )

            # Confirmar la transacción
            db_manager.connection.commit()
            print("Datos insertados con éxito.")

            # Preguntar si desea agregar otro artículo
            another = input("¿Desea agregar otro artículo? (s/n): ").strip().lower()
            if another != 's':
                break

    except sqlite3.Error as e:
        print(f"Error al insertar datos: {e}")

# Llamar a la función para insertar datos manualmente
insert_data_manually()

# Verificar los datos en la tabla articulos
db_manager.cursor.execute("SELECT * FROM articulos")
table = db_manager.cursor.fetchall()
for row in table:
    print(row)

# Cerrar la conexión
db_manager.close()