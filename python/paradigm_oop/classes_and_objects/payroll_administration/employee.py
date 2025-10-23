"""
This module defines the Employee class, 
which inherits from the Person class.
 
File: employee.py
Author: Anthony Bañon
Created: 2025-05-28
Last Updated: 2025-05-28
"""


from person import Person

class Employee(Person):
    def __init__(self, name, last_name, age, dni, file, antique):
        super().__init__(name, last_name, age, dni)
        self.file = file
        self.antique = antique

    # setter and getter
    

    def setFile(self, file):
        self.file = file
    
    def getFile(self):
        return self.file
    
    
    def setAntique(self, antique):
        self.antique = antique
    
    def getAntique(self):
        return self.antique
    
    
    def __str__(self):
        return f"\n{super().__str__()}\nFile: {self.file} \nAntique: {self.antique}"







    
