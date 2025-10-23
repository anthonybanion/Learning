"""
This module defines a Vehicle class that 
represents a vehicle with attributes such 
as make, model, year, and mileage.
 
File: vehiculo.py
Author: Anthony Bañon
Created: 2025-06-10
Last Updated: 2025-06-10
"""



class Vehicle():
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model= model 
        self.year = year
        self.mileage = mileage

    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make

    def ceroKM(self):
        self.mileage = 0
    
    def checkStatus(self):
        return self.mileage
    

