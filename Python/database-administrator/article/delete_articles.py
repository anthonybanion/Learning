#Brief: Delete data manually
#Description:  This file contains the function to delete data manually from the database.
#Date: 05/11/2024
#Author: Wilchez
#version: 1.0


from connection import DBConn
import sqlite3

db_manager = DBConn("sqlite/db_test.sqlite3")
db_manager.connect()

def delete_data_manually():
    try:
        # Solicitar al usuario que ingrese los datos
        while True:
            codigo = input("Por favor ingrese el código del artículo a eliminar: ")
            # Eliminar los datos en la tabla
            db_manager.cursor.execute(
                "DELETE FROM articulos WHERE codigo = ?",
                (codigo,)
            )

            # Confirmar la transacción
            db_manager.connection.commit()
            print(f"Artículo con código '{codigo}' eliminado con éxito.")

            # Preguntar si desea eliminar otro artículo
            another = input("¿Desea eliminar otro artículo? (s/n): ").strip().lower()
            if another != 's':
                break

    except sqlite3.Error as e:
        print(f"Error al eliminar datos: {e}")

# Llamar a la función para eliminar datos manualmente
delete_data_manually()

# Verificar los datos en la tabla articulos
db_manager.cursor.execute("SELECT * FROM articulos")
table = db_manager.cursor.fetchall()
for row in table:
    print(row)

# Cerrar la conexión
db_manager.close()