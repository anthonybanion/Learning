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
    

