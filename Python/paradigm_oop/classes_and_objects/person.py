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
    def setName(self):
        return self.name
    
    def getName(self, name):
        self.name=name
    


    def setName(self):
        return self.age
    
    def getName(self, age):
        self.age=age


    
    def setName(self):
        return self.last_name
    
    def getName(self, last_name):
        self.last_name=last_name
    
    
    
    def setName(self):
        return self.dni
    
    def getName(self, dni):
        self.dni=dni

    def __str__(self):
        return f"Name is: {self.name} \n Last Name: {self.last_name} \n Age: {self.age} \n Dni: {self.dni}"

    #method
    def isOlder(self):
        if self.age >= 18:
            print(f"Is Older whit age: {self.age} years")

person1=Person("Fredy", "Stevens", 35, "234567")

print(person1)

person1.isOlder()