"""
This module implements a car management system using OOP principles.

File: automotores.py
Author: Anthony Bañon
Created: 2025-06-10
Last Updated: 2025-06-10
"""


import os
import time

class Car:
    def __init__(self, brand, model, doors, fuel_level, mileage):
        self.brand = brand
        self.model = model
        self.doors = doors
        self.fuel_level = fuel_level  # in liters
        self.mileage = mileage        # in kilometers

    def __str__(self):
        return (f"Brand: {self.brand}, Model: {self.model}, Doors: {self.doors}, "
                f"Fuel: {self.fuel_level}L, Mileage: {self.mileage} km")

    def refuel(self, amount):
        self.fuel_level += amount
        return f"⛽ Current fuel level: {self.fuel_level}L"

    def start_engine(self):
        if self.fuel_level > 0:
            print("✅ Engine started successfully.")
        else:
            print("❌ Cannot start engine. Fuel tank is empty.")

    def drive_city(self):
        consumption = 10  # liters per 100 km in city
        if self.fuel_level >= consumption:
            self.fuel_level -= consumption
            self.mileage += 100
            return (f"🛣️ City drive complete. Fuel: {self.fuel_level}L | "
                    f"Mileage: {self.mileage} km")
        return "❌ Not enough fuel for 100 km city driving."

    def drive_highway(self):
        consumption = 8  # liters per 100 km on highway
        if self.fuel_level >= consumption:
            self.fuel_level -= consumption
            self.mileage += 100
            return (f"🛤️ Highway drive complete. Fuel: {self.fuel_level}L | "
                    f"Mileage: {self.mileage} km")
        return "❌ Not enough fuel for 100 km highway driving."

    def city_range(self):
        return f"🔋 Estimated city range: {self.fuel_level * 10} km"

    def highway_range(self):
        return f"🔋 Estimated highway range: {self.fuel_level * 12.5} km"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# --- Main Program ---
def main():
    car = Car("Ford", "Fiesta", 4, 90, 200)

    try:
        fuel = int(input("Enter the amount of fuel to add (L): "))
        print(car.refuel(fuel))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

    car.start_engine()
    time.sleep(2)
    clear_screen()

    print("""
Select a driving option:
1. Drive 100 km in city
2. Drive 100 km on highway
3. Skip
    """)
    try:
        choice = int(input("Your choice: "))
        if choice == 1:
            print(car.drive_city())
        elif choice == 2:
            print(car.drive_highway())
        else:
            print("ℹ️ No driving performed.")
    except ValueError:
        print("❌ Invalid choice.")

    time.sleep(2)
    clear_screen()

    print("""
Check range:
1. City range
2. Highway range
3. Skip
    """)
    try:
        choice = int(input("Your choice: "))
        if choice == 1:
            print(car.city_range())
        elif choice == 2:
            print(car.highway_range())
        else:
            print("ℹ️ No range check performed.")
    except ValueError:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
