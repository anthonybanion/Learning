# This file is part of a Python project demonstrating OOP principles.
# File: person.py
# Created: 2024-11-05  
# Last Updated: 2025-06-10
# Version: 1.0.1


from abc import ABC, abstractmethod

# Base class
class Person:
    def __init__(self, first_name, last_name, dni, age):
        self.first_name = first_name
        self.last_name = last_name
        self.dni = dni
        self.__age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.dni} {self.__age}'

    # Getters
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_dni(self):
        return self.dni
    
    def get_age(self):
        return self.__age

    # Setters
    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_dni(self, dni):
        self.dni = dni

    def set_age(self, age):
        self.__age = age

    # Custom methods
    def speak(self):
        return f'Hi, I am {self.first_name} {self.last_name} and I am {self.__age} years old.'
    
    def is_adult(self):
        return self.__age >= 18
    
    def introduce(self):
        return f'Hi, I am {self.first_name} {self.last_name}'


# Abstract class for skills
class Skill(ABC):
    @abstractmethod
    def sing(self):
        pass

    @abstractmethod
    def dance(self):
        pass


# Employee class
class Employee(Person, Skill):
    def __init__(self, first_name, last_name, dni, age, salary, seniority, employee_id):
        super().__init__(first_name, last_name, dni, age)
        self.salary = salary
        self.seniority = seniority
        self.employee_id = employee_id

    def __str__(self):
        return f'{super().__str__()} {self.salary} {self.seniority} {self.employee_id}'

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def speak(self):
        return super().speak() + f', with {self.seniority} years of seniority and a salary of {self.salary}.'

    def has_vacation(self):
        return 'Has vacation' if self.seniority > 5 else 'No vacation'

    def bonus(self):
        return self.salary * 0.1 if self.seniority > 5 else self.salary * 0.05

    def sing(self):
        return 'Employee sings'

    def dance(self):
        return 'Employee dances'


# Administrator class
class Administrator(Person, Skill):
    def __init__(self, first_name, last_name, dni, age, position):
        super().__init__(first_name, last_name, dni, age)
        self.position = position

    def __str__(self):
        return f'{super().__str__()} {self.position}'

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def speak(self):
        return super().speak() + ' and I am an administrator.'

    def sing(self):
        return 'Administrator sings'

    def dance(self):
        return 'Administrator dances'


# Student class
class Student(Person):
    def __init__(self, first_name, last_name, dni, age, student_id, career, year):
        super().__init__(first_name, last_name, dni, age)
        self.student_id = student_id
        self.career = career
        self.year = year

    def __str__(self):
        return f'{super().__str__()} {self.student_id} {self.career} {self.year}'


# Example usage
student1 = Student("Mario", "Perez", "23423", 45, "2423", "Systems Analyst", 3)
print(student1)

employee1 = Employee("John", "Smith", 12345678, 30, 50000, 5, 1234)
admin1 = Administrator("Smith", "John", 12345678, 30, "Manager")

# This line does nothing due to name mangling
employee1.__age = 25  # Incorrect way to set private attribute
employee1.set_age(25)  # Correct way

print(employee1)
print(admin1)

print(employee1.dance())
print(admin1.dance())
print(employee1.sing())
print(admin1.sing())

if employee1.is_adult():
    print('Is an adult')
else:
    print('Is not an adult')
