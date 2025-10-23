#Brief: Insert a Person in the database
#Date: 05/11/2024
#Version: 1.0

import sqlite3
from connection.connection import openConnection


def createPerson(id,nombre,apellido,dni):
    conexion = openConnection()
    cursor=conexion.cursor()

    cursor.execute(''' INSERT INTO personas VALUES(?,?,?,?)''',(id,nombre, apellido, dni))
    conexion.commit()
    conexion.close()

