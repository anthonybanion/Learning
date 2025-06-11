"""
This script defines a simple Peewee ORM model for a "Person" entity,
 
File: people.py
Author: Anthony Bañon
Created: 2025-06-10
Last Updated: 2025-06-10
"""


from peewee import *
from playhouse.mysql_ext import MySQLDatabase



# Conexión a la base de datos
# db = SqliteDatabase('people.db')
db =  MySQLDatabase('people',
                   user='root',
                   password='',
                   host='127.0.0.1',
                   port=3306)



class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.
    
db.connect()
db.create_tables([Person])


persona1=Person.create(name='Alejandro', birthday='1995-12-12')
persona2=Person.create(name='Juan', birthday='1990-12-12')
persona1.save()
persona2.save()