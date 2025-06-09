"""
This script demonstrates a simple payroll 
administration system using classes and objects.
 
File: main.py
Author: Anthony Bañon
Created: 2025-05-28
Last Updated: 2025-05-28
"""


from employee import Employee
from salary import Salary
from vacation import Vacation



employe1 = Employee("Alberto", "Peres", 45, 23498713, 1234,21)

print(employe1)
salary1 = Salary(employe1)
print(salary1.calculate_salary())

vacation1 = Vacation(employe1)
print(vacation1.calculate_vacation_days())





