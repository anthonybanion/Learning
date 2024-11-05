import sqlite3 

def obtenerdatos(cursor):
    cursor.execute("SELECT * FROM cliente")
    registros = cursor.fetchall()
    print("Registros de la tabla cliente")
    for row in registros:
        print("id: ", row[0])
        print("cliente. ", row[1], row[2])

try: 
    connection = sqlite3.connect("./extra/prueba/database/cliente.db") 
    cursor = connection.cursor() 
    print("conectada") 
    obtenerdatos(cursor) 

except sqlite3.Error as e: 
    print("Error: ", e) 

finally: 
    cursor.close() 
    connection.close() 