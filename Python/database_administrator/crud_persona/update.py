#Brief: Update a Person in the database
#Date: 05/11/2024
#Version: 1.0

import sqlite3
from create import create

def update():
    conexion=sqlite3.connect('./extra/database/crud/crud.db')
    cursor=conexion.cursor()
    cursor.execute('''
    UPDATE personas SET nombre='Juan' WHERE id_persona=2
    '''
    )
    conexion.commit()
    conexion.close()

update()