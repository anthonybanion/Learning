"""
Description: This program generates a multiplication table for a given number using static attribute.
 
File: multiplicationTableWithStaticAttribute.py
Author: Anthony Bañon
Created: 2025-04-18
Last Updated: 2025-04-18
"""

from tkinter import *
from tkinter import ttk

class MultiplicationApp:
    entry_number = None  # Static attribute

    @staticmethod  
    def generate_table():
        """
        Description: Generates a multiplication table for the number entered in the entry field.
        
        Args:
            param (int): The number for which the multiplication table is generated.
        
        Returns:
            str: The generated multiplication table as a string.
        
        Raises:
            Exception: ValueError if the input is not a valid integer.
        """
         
        try:
            number = int(MultiplicationApp.entry_number.get())  # Access to the static attribute
            # join the multiplication results into a single string
            table = "\n".join([f"{number} x {i} = {number * i}" for i in range(1, 13)])
            # Display the result in the label
            MultiplicationApp.result.config(text=table)
        except ValueError:
            # If the input is not a valid integer, display an error message
            MultiplicationApp.result.config(text="Please enter a valid number.")

root = Tk()
MultiplicationApp.entry_number = Entry(root)
MultiplicationApp.entry_number.pack(pady=10)

MultiplicationApp.result = ttk.Label(root, text="", font=("Arial", 14))
MultiplicationApp.result.pack(pady=10)

button = ttk.Button(root, text="Generate", command=MultiplicationApp.generate_table)
button.pack(pady=10)

root.mainloop()