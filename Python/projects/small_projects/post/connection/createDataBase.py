#Brief: Create the tables in the database
#Date: 05/11/2024
#Version: 1.0


import sqlite3
from connection import openConnection

def create():
    conexion = openConnection()
    cursor=conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS "personas" (
                    "id_persona"	INTEGER NOT NULL UNIQUE,
                    "nombre"	TEXT NOT NULL,
                    "apellido"	TEXT NOT NULL,
                    "dni"	TEXT NOT NULL UNIQUE,
                    PRIMARY KEY("id_persona" AUTOINCREMENT))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS "usuarios" (
                    "id_usuario"	INTEGER NOT NULL UNIQUE,
                    "usuario"	TEXT NOT NULL,
                    "contrasenia"	TEXT NOT NULL,
                    "id_persona"	INTEGER NOT NULL UNIQUE,
                    FOREIGN KEY("id_persona") REFERENCES "personas"("id_persona"),
                    PRIMARY KEY("id_usuario" AUTOINCREMENT))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS "mensajes" (
                    "id_mensaje"	INTEGER NOT NULL UNIQUE,
                    "emisor"	INTEGER NOT NULL,
                    "receptor"	INTEGER NOT NULL,
                    "asunto"	TEXT NOT NULL,
                    "mensaje"	TEXT NOT NULL,
                    "adjunto"	TEXT,
                    "fecha"	TEXT NOT NULL,
                    "hora"	TEXT NOT NULL,
                    FOREIGN KEY("receptor") REFERENCES "usuarios"("id_usuario"),
                    FOREIGN KEY("emisor") REFERENCES "usuarios"("id_usuario"),
                    PRIMARY KEY("id_mensaje" AUTOINCREMENT))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS "posteos" (
                    "id_posteo"	INTEGER NOT NULL UNIQUE,
                    "texto"	TEXT NOT NULL,
                    "multimedia"	TEXT,
                    "fecha"	TEXT NOT NULL,
                    "hora"	TEXT NOT NULL,
                    "id_usuario"	INTEGER NOT NULL,
                    PRIMARY KEY("id_posteo" AUTOINCREMENT)
                    FOREIGN KEY("id_usuario") REFERENCES "usuarios"("id_usuario"))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS "posteos_x_usuarios" (
                    "id_posteo_x_usuario"	INTEGER NOT NULL UNIQUE,
                    "id_posteo"	INTEGER NOT NULL,
                    "id_usuario"	INTEGER NOT NULL,
                    FOREIGN KEY("id_usuario") REFERENCES "usuarios"("id_usuario"),
                    PRIMARY KEY("id_posteo_x_usuario" AUTOINCREMENT),
                    FOREIGN KEY("id_posteo") REFERENCES "posteos"("id_posteo"))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS "comentaros" (
                    "id_comentario"	INTEGER NOT NULL UNIQUE,
                    "comentario"	TEXT NOT NULL,
                    "fecha"	TEXT NOT NULL,
                    "hora"	TEXT NOT NULL,
                    "id_usuario"	INTEGER NOT NULL,
                    "id_posteo"	INTEGER NOT NULL,
                    FOREIGN KEY("id_posteo") REFERENCES "posteos"("id_posteo"),
                    FOREIGN KEY("id_usuario") REFERENCES "usuarios"("id_usuario"),
                    PRIMARY KEY("id_comentario" AUTOINCREMENT))''')

    conexion.commit()
    conexion.close()
    return print(f"La tabla a sido creada")

create()