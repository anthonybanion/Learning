"""
Description: the Person class, which represents a human being.

File: person.py
Author: Anthony Bañon
Created: 2025-05-14
Last Updated: 2025-05-14
"""


class Person():
    def __init__(self, name, last_name, age, dni):
        self.name=name
        self.last_name=last_name
        self.age=age
        self.dni=dni

    # setter and getter
    def setName(self, name):
        self.name=name

    def getName(self):
        return self.name
    

    def setAge(self, age):
        self.age=age

    def getAge(self):
        return self.age
    

    def setLastName(self, last_name):
        self.last_name=last_name

    def getLastName(self):
        return self.last_name
    

    def setDni(self, dni):
        self.dni=dni

    def getDni(self):
        return self.dni
    

    #method
    def isOlder(self):
        if self.age >= 18:
            print(f"Is Older whit age: {self.age} years")

    # string representation
    def __str__(self):
        return f"Name is: {self.name} \nLast Name: {self.last_name} \nAge: {self.age} \nDni: {self.dni}"

    
