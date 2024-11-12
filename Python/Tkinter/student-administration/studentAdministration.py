#Briefa: Create a CRUD with sqlite3
#Date: 05/11/2024
#version: 1.0

import sqlite3

def abrir_conexion():
    conexion=sqlite3.connect('Python/Tkinter/student-administration/alumnos.db')
    return conexion


def crear_tabla_alumnos():
    conexion = abrir_conexion()
    cursor=conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS "alumnos" (
                    "id" INTEGER NOT NULL UNIQUE,
                    "nombre" TEXT NOT NULL,
                    "apellido" TEXT NOT NULL,
                    "dni" TEXT NOT NULL UNIQUE,
                    PRIMARY KEY("id" AUTOINCREMENT))''')

    conexion.commit()
    conexion.close()
    return print(f"La tabla a sido creada")




def crear_alumnos(id,nombre,apellido,dni):
    conexion = abrir_conexion()
    cursor=conexion.cursor()

    cursor.execute(''' INSERT INTO alumnos VALUES(?,?,?,?)''',(id, nombre, apellido, dni))
    conexion.commit()
    conexion.close()


def listar_alumnos():
    conexion = abrir_conexion()
    cursor=conexion.cursor()

    cursor.execute(''' SELECT * FROM alumnos''')
    lista=cursor.fetchall()
    # for row in lista:
    #     print(f'id: {row[0]}')
    #     print(f'nombre: {row[1]}')
    #     print(f'apellido: {row[0]}')
    #     print(f'dni: {row[0]}')
    #     print('----------')

    conexion.commit()
    conexion.close()
    return lista

def eliminar_alumnos(id):
    conexion = abrir_conexion()
    cursor=conexion.cursor()
    cursor.execute("DELETE alumnos SET nombre='GABI' WHERE id=?",(id))
    conexion.commit()
    conexion.close()

def editar_alumnos(id, nombre, apellido, dni):
    conexion = abrir_conexion()
    cursor=conexion.cursor()
    cursor.execute("UPDATE alumnos SET nombre=? WHERE id=?",(nombre,id))
    cursor.execute("UPDATE alumnos SET apellido=? WHERE id=?",(apellido,id))
    cursor.execute("UPDATE alumnos SET dni=? WHERE id=?",(dni,id))
    conexion.commit()
    conexion.close()

def buscar_alumnos(id):
    conexion = abrir_conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM alumnos WHERE id=?",(id,))
    lista=cursor.fetchall()
    # for row in lista:
    #     print(f'id: {row[0]}')
    #     print(f'nombre: {row[1]}')
    #     print(f'apellido: {row[2]}')
    #     print(f'dni: {row[3]}')
    #     print('----------')
    conexion.commit()
    conexion.close()
    return lista