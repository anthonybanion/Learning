"""
Description: This program generates a multiplication table for a given number using Classes.
 
File: multiplicationTableClass.py
Author: Anthony Bañon
Created: 2025-04-18
Last Updated: 2025-04-18
"""


from tkinter import *
from tkinter import ttk

class MultiplicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiplication Table")  

        self.title_label = ttk.Label(root, text="Multiplication Table", font=("Arial", 20))
        self.title_label.pack(pady=10)

        self.entry_number = Entry(root)
        self.entry_number.pack(pady=10)

        self.button = ttk.Button(root, text="Generate", command=self.generate_table)
        self.button.pack(pady=10)

        self.result = ttk.Label(root, text="", font=("Arial", 14))
        self.result.pack(pady=10)

    def generate_table(self):
        """
        Description: Generates a multiplication table for the number entered in the entry field.
        
        Args:
            number (int): The number for which the multiplication table is generated.
        
        Returns:
            str: The generated multiplication table as a string.
        
        Raises:
            Exception: If the input is not a valid integer.
        """
        
        try:
            number = int(self.entry_number.get())
            # join the multiplication results into a single string
            table = "\n".join([f"{number} x {i} = {number * i}" for i in range(1, 13)])
            # Display the result in the label
            self.result.config(text=table)
        except ValueError:
            # If the input is not a valid integer, display an error message
            self.result.config(text="Please enter a valid number.")

# Create the main window
root = Tk()
app = MultiplicationApp(root)
root.mainloop()