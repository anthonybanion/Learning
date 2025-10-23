"""
This module implements an e-commerce system using OOP principles.
 
File: ecommerce2.py
Author: Anthony Bañon
Created: 2025-06-10
Last Updated: 2025-06-10
"""


from abc import ABC, abstractmethod

# Abstract class: Person
class Person(ABC):
    def __init__(self, name, email):
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @abstractmethod
    def show_info(self):
        pass

# Class: Customer (inherits from Person)
class Customer(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self._order_history = []

    def show_info(self):
        return f"Customer: {self._name}, Email: {self._email}"

    def add_order(self, order):
        self._order_history.append(order)

    @property
    def order_history(self):
        return self._order_history

# Class: Employee (inherits from Person)
class Employee(Person):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self._role = role
        self._sales_count = 0

    def show_info(self):
        return f"Employee: {self._name}, Email: {self._email}, Role: {self._role}"

    def register_sale(self):
        self._sales_count += 1

    @property
    def sales_count(self):
        return self._sales_count

# Class: Product
class Product:
    def __init__(self, name, price, stock):
        self._name = name
        self._price = price
        self._stock = stock

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative")

    @property
    def stock(self):
        return self._stock

    def reduce_stock(self, quantity):
        if quantity <= self._stock:
            self._stock -= quantity
        else:
            raise ValueError("Insufficient stock")

    def __str__(self):
        return f"{self._name}: ${self._price}, Stock: {self._stock}"

# Class: Cart (Composition)
class Cart:
    def __init__(self):
        self._items = []

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self._items.append((product, quantity))
        else:
            raise ValueError(f"Not enough stock for {product.name}")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self._items)

    def clear(self):
        self._items.clear()

    @property
    def items(self):
        return self._items

# Class: Order (Aggregation)
class Order:
    def __init__(self, customer, cart):
        self._customer = customer
        self._items = cart.items
        self._total = cart.calculate_total()

    def process_order(self):
        for product, quantity in self._items:
            product.reduce_stock(quantity)

    def __str__(self):
        details = "\n".join([f"{product.name} x{quantity}" for product, quantity in self._items])
        return f"Order for {self._customer.name}:\n{details}\nTotal: ${self._total:.2f}"

# Usage example
if __name__ == "__main__":
    # Create products
    p1 = Product("Laptop", 1500, 10)
    p2 = Product("Headphones", 100, 50)
    p3 = Product("Mouse", 25, 100)

    # Create customer
    customer = Customer("John Doe", "john@gmail.com")

    # Create cart
    cart = Cart()
    cart.add_product(p1, 1)
    cart.add_product(p2, 2)

    # Create order
    order = Order(customer, cart)
    order.process_order()
    customer.add_order(order)

    # Show order info
    print(order)

    # Create employee
    employee = Employee("Anna Smith", "anna@gmail.com", "Salesperson")
    employee.register_sale()

    # Show people info
    print(customer.show_info())
    print(employee.show_info())
