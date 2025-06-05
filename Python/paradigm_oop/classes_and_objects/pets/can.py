"""
Description: The Can class, which represents a dog.
 
File: can.py
Author: Anthony Bañon
Created: 2025-05-14
Last Updated: 2025-05-14
"""


class Can:
    def __init__(self, name, age, race, owner):
        self._name=name
        self._age=age
        self.race=race
        self.owner=owner
    
    # getter and setter
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._age
    
    def setName(self, age):
        self._age = age
    
    def getName(self):
        return self.race
    
    def setName(self, race):
        self.race = race

    def getName(self):
        return self.owner
    
    def setName(self, owner):
        self.owner = owner
    
    def __str__(self):
        return f"name is: {self._name} \n age: {self._age} \n race: {self.race} \n owner is: {self.owner}"

    #methods
    def run():
        print("The dog is running")
    
    def bark():
        print("The dog is barking")
    
    def eat():
        print("The dog is eating")
    
    def sleep():
        print("The dog is sleeping")

can1 = Can("Lucky", 5, "Shih Tzu", "Anthony")
can2 = Can("Shadow", 10, "Doberman", "Enrique")

print(can1)
print(can2)



  
    

