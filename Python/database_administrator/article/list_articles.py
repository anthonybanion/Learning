#Brief: List articles
#Description:  This file contains the function to list all the articles in the database.
#Date: 05/11/2024
#Author: Wilchez
#version: 1.0


from connection import DBConn
import sqlite3

db_manager = DBConn("sqlite/db_test.sqlite3")
db_manager.connect()

db_manager.cursor.execute("SELECT * FROM articulos")
table = db_manager.cursor.fetchall()
for row in table:
    print(row)

# Cerrar la conexión
db_manager.close()

