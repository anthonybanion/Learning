"""
Description: This program generates a multiplication table.
 
File: multiplicationTable.py
Author: Anthony Bañon
Created: 2025-04-18
Last Updated: 2025-04-18
"""

from tkinter import *
from tkinter import ttk
root = Tk()  # Create the main window
title_label =ttk.Label(root, text="Multiplication Table", font=("Arial", 20))  
title_label.pack(pady=10)

entry_number = Entry(root) 
entry_number.pack(pady=10)  # Adds vertical padding

def generate_table():
    """
    Description: Generate the multiplication table for a given number.
    
    Args:
        number (int): The number for which the multiplication table is generated.
    
    Returns:
        str: The generated multiplication table as a string.
    
    Raises:
        Exception: If the input is not a valid integer.
    """
    
    try:
        number = int(entry_number.get())
        # join the multiplication results into a single string
        table = "\n".join([f"{number} x {i} = {number * i}" for i in range(1, 13)])
        # Display the result in the label
        result.config(text=table)
    except ValueError:
        result.config(text="Please enter a valid number.")

button = ttk.Button(root, text="Generate", command=generate_table)
button.pack(pady=10)
# Create a label to display the result
result = ttk.Label(root, text="", font=("Arial", 14))
result.pack(pady=10)


root.mainloop()