#Brief: Download a Person in the database
#Date: 05/11/2024
#Version: 1.0

import sqlite3
from create import create

def download():
    conexion=sqlite3.connect('./extra/database/crud/crud.db')
    cursor=conexion.cursor()
    cursor.execute('''
    INSERT INTO personas VALUES('2','Rosa','9876534')
    '''
    )
    conexion.commit()
    conexion.close()

download()
