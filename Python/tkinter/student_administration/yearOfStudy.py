#Briefa: year of study
#Date: 05/11/2024
#version: 1.0

import sqlite3

def abrir_conexion():
    conexion=sqlite3.connect('Python/Tkinter/student-administration/alumnos.db')
    return conexion


def crear_tabla_yearOftudy():
    conexion = abrir_conexion()
    cursor=conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS "yearOftudy" (
                    "id" INTEGER NOT NULL UNIQUE,
                    "year" TEXT NOT NULL,
                    PRIMARY KEY("id" AUTOINCREMENT))''')
    conexion.commit()
    conexion.close()
    return print(f"La tabla a sido creada")




# def crear_yearOftudy():
#     conexion = abrir_conexion()
#     cursor=conexion.cursor()

#     cursor.execute(''' INSERT INTO yearOftudy(id, year) VALUES("1","primero"),("2","segundo"),("3","tercero") ''')
#     conexion.commit()
#     conexion.close()


def listar_yearOftudy():
    conexion = abrir_conexion()
    cursor=conexion.cursor()

    cursor.execute(''' SELECT * FROM yearOftudy''')
    lista=cursor.fetchall()
    # for row in lista:
    #     print(f'id: {row[0]}')
    #     print(f'nombre: {row[1]}')
    #     print('----------')

    conexion.commit()
    conexion.close()
    return lista

def eliminar_yearOftudy(id):
    conexion = abrir_conexion()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM yearOftudy WHERE id=? ",(id,))
    conexion.commit()
    conexion.close()

# abrir_conexion()
# crear_tabla_yearOftudy()

# listar_yearOftudy()

