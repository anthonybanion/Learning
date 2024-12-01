#Brief: Create a Article in the database
#Description: This file contains the connection to the database, the creation of the table, and the display of the tables in the database.
#Date: 05/11/2024
#Author: Wilchez
#version: 1.0


import sqlite3

class DBConn:
    #Inicializador de las variables
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        
    #Conección a la BD y abre cursor
    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    #Crea la tabla en la BD en caso de no existir
    def create_table(self):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS articulos (id INTEGER PRIMARY KEY AUTOINCREMENT, codigo TEXT, nombre TEXT, stock INTEGER, detalle TEXT)")

    #Muestra las tablas, el criterio de busqueda es desde el master de sqlite busca tipo tabla, si tengo 2, va a listar las 2
    def show_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()

        #Recorrido de todas las tablas en la db
        print("Tables in the database:")
        for table in tables:
            print(table[0])

    
    #Se cierra el cursor (siempre cerrarlo)
    def close(self):
        if self.cursor:
            self.cursor.close()
    #Se cierra la conexión
        if self.connection:
            self.connection.close()

#Invoco a la clase (objeto DBConn que contiene todas esas funciones)
db_manager = DBConn("sqlite/db_test.sqlite3")

#Call de cada función dentro de la clase DBConn (Siempre invocarlas, sino no se ejecuta.)
db_manager.connect()
db_manager.create_table()
db_manager.show_tables()
db_manager.close()


    
    