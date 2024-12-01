#Brief: Create tables in the database email
#Date: 05/11/2024
#Version: 1.0

import sqlite3
conexion=sqlite3.connect('./extra/database/email.db')
cursor=conexion.cursor()
cursor.execute('''
CREATE TABLE App_correos(
	"id_app_correo"	INTEGER NOT NULL UNIQUE,
	"spam"	TEXT NOT NULL,
	"borrador"	TEXT NOT NULL,
	"estado"	TEXT NOT NULL,
	PRIMARY KEY("id_app_correo" AUTOINCREMENT)
)'''
)
cursor.execute('''
CREATE TABLE personas(
	"id_persona"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL,
	"apellido"	TEXT NOT NULL,
	"telefono"	TEXT NOT NULL,
	"id_app_correo"	INTEGER NOT NULL,
	FOREIGN KEY("id_app_correo") REFERENCES "App_correo"("id_app_correo"),
	PRIMARY KEY("id_persona" AUTOINCREMENT)
)'''
)
cursor.execute('''
CREATE TABLE usuarios(
	"id_usuario"	INTEGER NOT NULL UNIQUE,
	"direccion_coreo"	TEXT NOT NULL UNIQUE,
	"contraseña"	TEXT NOT NULL,
	"rol"	TEXT NOT NULL,
	"id_persona"	INTEGER NOT NULL,
	FOREIGN KEY("id_persona") REFERENCES "personas"("id_persona"),
	PRIMARY KEY("id_usuario" AUTOINCREMENT)
)'''
)
cursor.execute('''
CREATE TABLE recibir(
	"id_recibir"	INTEGER NOT NULL UNIQUE,
	"id_usuario"	INTEGER NOT NULL,
	"id_mensaje"	INTEGER NOT NULL,
	FOREIGN KEY("id_usuario") REFERENCES "usuarios"("id_usuario"),
	FOREIGN KEY("id_mensaje") REFERENCES "mensajes"("id_mensaje"),
	PRIMARY KEY("id_recibir" AUTOINCREMENT)
)'''
)
cursor.execute('''
CREATE TABLE mensajes(
	"id_mensaje"	INTEGER NOT NULL UNIQUE,
	"emisor"	TEXT NOT NULL,
	"destinatario"	TEXT NOT NULL,
	"asunto"	TEXT NOT NULL,
	"CC"	TEXT DEFAULT Null,
	"CCO"	TEXT DEFAULT Null,
	"mensaje"	TEXT NOT NULL,
	"adjunto"	TEXT DEFAULT Null,
	"id_usuario"	INTEGER NOT NULL,
	FOREIGN KEY("id_usuario") REFERENCES "usuarios"("id_usuario"),
	PRIMARY KEY("id_mensaje" AUTOINCREMENT)
)'''
)

conexion.commit()
conexion.close()