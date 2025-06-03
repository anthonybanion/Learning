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