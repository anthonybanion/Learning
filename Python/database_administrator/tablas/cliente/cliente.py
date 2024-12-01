import sqlite3
conexion=sqlite3.connect('./extra/prueba/database/cliente/base.db')
cursor=conexion.cursor()
cursor.execute('''
CREATE TABLE if NOT EXISTS cliente(
    id integer primary key autoincrement,
    nombre text,
    email text
)'''
)
cursor.execute('''
insert into cliente(nombre,email) values('Juan','juan@correo'),('Pedro','pedro@correo'),('Laura','laura@correo') 
'''
)

conexion.commit()
conexion.close()