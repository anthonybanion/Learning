#Brief: List persons
#Date: 05/11/2024
#Version: 1.0

import sqlite3

def list():
    conexion=sqlite3.connect('./extra/database/crud/crud.db')
    cursor=conexion.cursor()
    cursor.execute('SELECT * FROM personas')
    personas=cursor.fetchall()
    for persona in personas:
        print(persona)
    conexion.close()

list()
