"""
This module defines the Salary class, which 
calculates the salary of an employee based on 
their years of service.
 
File: salary.py
Author: Anthony Bañon
Created: 2025-05-28
Last Updated: 2025-05-28
"""



class Salary:
    def __init__(self, employee):
        self.salary = 0.0
        self.employee = employee
    
    def calculate_salary(self):
        BASE = 1000
        if self.employee.getAntique()<5:
            self.salary = BASE * 1.25
        elif self.employee.getAntique()>=5 and self.employee.getAntique()<10:
            self.salary = BASE * 1.5
        elif self.employee.getAntique()>=10 and self.employee.getAntique()<15:
            self.salary = BASE * 1.75
        elif self.employee.getAntique()>=15 and self.employee.getAntique()<20:
            self.salary = BASE * 2.0
        elif self.employee.getAntique()>=20:
            self.salary = BASE * 2.25
        else:
            raise ValueError("Invalid file type")
        
        return f"Salary: {self.salary}"

