#Brief: Create tables in the database for the student
#Date: 05/11/2024
#Version: 1.0

import sqlite3
conexion=sqlite3.connect('alumno.db')
cursor=conexion.cursor()
cursor.execute('''
CREATE TABLE alumno(
	"id_alumno"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL,
	"apellido"	TEXT NOT NULL,
    PRIMARY KEY("id_alumno" AUTOINCREMENT)
)'''
)

cursor.execute('''
CREATE TABLE curso(
	"id_curso"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL,
	"nota"	    INTEGER NOT NULL,
    "id_alumno"	INTEGER NOT NULL,
    PRIMARY KEY("id_curso" AUTOINCREMENT),
    FOREIGN KEY("id_alumno") REFERENCES "alumno"("id_alumno")
)'''
)


conexion.commit()
conexion.close()