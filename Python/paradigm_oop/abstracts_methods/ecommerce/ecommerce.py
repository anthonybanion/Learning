"""
This module implements an e-commerce system using 
OOP principles such as encapsulation, inheritance, 
polymorphism, composition, and aggregation.
 
File: ecommerce.py
Author: Anthony Bañon
Created: 2025-06-10
Last Updated: 2025-06-10
"""


from abc import ABC, abstractmethod

# Abstract class: Person
class Person(ABC):
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    @abstractmethod
    def display_info(self):
        pass

# Client class (inherits from Person)
class Client(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self.order_history = []  # List of past orders

    def display_info(self):
        return f"Client: {self.name}, ID: {self.id_number}"

    def add_order(self, order):
        self.order_history.append(order)

# Employee class (inherits from Person)
class Employee(Person):
    def __init__(self, name, id_number, position):
        super().__init__(name, id_number)
        self.position = position
        self.sales_count = 0

    def display_info(self):
        return f"Employee: {self.name}, ID: {self.id_number}, Position: {self.position}"

    def register_sale(self):
        self.sales_count += 1

# Product class
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price  # Encapsulation
        self.__stock = stock  # Encapsulation

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self.__price = new_price

    @property
    def stock(self):
        return self.__stock

    def decrease_stock(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
        else:
            raise ValueError("Insufficient stock")

    def __str__(self):
        return f"{self.name}: ${self.__price}, Stock: {self.__stock}"

# Cart class (Composition)
class Cart:
    def __init__(self):
        self.items = []  # List of (product, quantity) tuples

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
        else:
            raise ValueError(f"Not enough stock for {product.name}")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def clear(self):
        self.items.clear()

# Order class (Aggregation)
class Order:
    def __init__(self, client, cart):
        self.client = client
        self.items = cart.items  # Aggregation of products
        self.total = cart.calculate_total()

    def process_order(self):
        for product, quantity in self.items:
            product.decrease_stock(quantity)

    def __str__(self):
        details = "\n".join([f"{product.name} x{quantity}" for product, quantity in self.items])
        return f"Order for {self.client.name}:\n{details}\nTotal: ${self.total:.2f}"

# Example usage
if __name__ == "__main__":
    # Create products
    laptop = Product("Laptop", 1500, 10)
    headphones = Product("Headphones", 100, 50)
    mouse = Product("Mouse", 25, 100)

    # Create client
    client = Client("John Smith", "12345678")

    # Create cart
    cart = Cart()
    cart.add_product(laptop, 1)
    cart.add_product(headphones, 2)

    # Create order
    order = Order(client, cart)
    order.process_order()
    client.add_order(order)

    # Print order information
    print(order)

    # Create employee
    employee = Employee("Anna Lopez", "ana@gmail.com", "Sales Representative")
    employee.register_sale()

    # Print person info
    print(client.display_info())
    print(employee.display_info())
