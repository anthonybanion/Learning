#Brief: Create a Person in the database
#Date: 05/11/2024
#Version: 1.0

import sqlite3

def create():
    conexion=sqlite3.connect('./extra/database/crud/crud.db')
    cursor=conexion.cursor()
    cursor.execute('''
    CREATE TABLE if NOT EXISTS personas(
        "id_persona"	INTEGER NOT NULL UNIQUE,
        "nombre"	TEXT NOT NULL,
        "dni"    TEXT NOT NULL
    )'''
    )
    conexion.commit()
    conexion.close()

create()