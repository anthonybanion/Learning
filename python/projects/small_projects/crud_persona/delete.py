#Brief: Delete a Person in the database
#Date: 05/11/2024
#Version: 1.0

import sqlite3

def delete():
    conexion=sqlite3.connect('./extra/database/crud/crud.db')
    cursor=conexion.cursor()
    cursor.execute('''
    DELETE FROM personas WHERE id_persona=1
    '''
    )
    conexion.commit()
    conexion.close()

delete()