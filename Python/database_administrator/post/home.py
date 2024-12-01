#Brief: Create a Person in the database
#Date: 05/11/2024
#Version: 1.0

from user.createUser import createPerson

id=int(input("id: "))
nombre=input("nombre: ")
apellido=input("apellido: ")
dni=input("dni: ")
createPerson(id, nombre, apellido, dni)