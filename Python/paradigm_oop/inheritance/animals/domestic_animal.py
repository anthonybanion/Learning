"""
This module defines classes for domestic animals, 
demonstrating inheritance and polymorphism.

File: domestic_animal.py
Author: Anthony Bañon
Created: 2025-06-10
Last Updated: 2025-06-10
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

    def eat(self):
        return f"{self.name} is eating."

    def __str__(self):
        return f"{self.name} is an animal."

class Dog(Animal):
    def speak(self):
        return "Woof!"

    def __str__(self):
        return f"{self.name} is a dog."

class Cat(Animal):
    def speak(self):
        return "Meow!"

    def __str__(self):
        return f"{self.name} is a cat."



if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    print(dog)  # Buddy is a dog.
    print(dog.speak())  # Woof!
    print(dog.eat())  # Buddy is eating.

    print(cat)  # Whiskers is a cat.
    print(cat.speak())  # Meow!
    print(cat.eat())  # Whiskers is eating.