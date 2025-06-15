"""
This module defines the Vacation class, 
which calculates the vacation days of an 
employee based on their years of service.
  
File: vacation.py
Author: Anthony Bañon
Created: 2025-05-28
Last Updated: 2025-05-28
"""



class Vacation:
    def __init__(self, employee):
        self.employee = employee
        self.vacation_days = 0

    def calculate_vacation_days(self):
        if self.employee.getAntique() < 5:
            self.vacation_days = 14
        elif self.employee.getAntique() >= 5 and self.employee.getAntique() < 10:
            self.vacation_days = 21
        elif self.employee.getAntique() >= 10 and self.employee.getAntique() < 15:
            self.vacation_days = 28
        elif self.employee.getAntique() >= 15 and self.employee.getAntique() < 25:
            self.vacation_days = 35
        elif self.employee.getAntique() >= 25 and self.employee.getAntique() < 35:
            self.vacation_days = (self.employee.getAntique() - 25) + 35
        elif self.employee.getAntique() >= 35:
            self.vacation_days = 45
        else:
            raise ValueError("Invalid antique value")

        return f"Vacation Days: {self.vacation_days}"


