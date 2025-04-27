"""
Description: This program calculates the final price of a product including VAT with OOP.
 
File: vatCalculationClass.py
Author: Anthony Bañon
Created: 2025-04-26
Last Updated: 2025-04-26
"""



from tkinter import *
from tkinter import ttk

class VatCalculationApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")  
        self.root.title("VAT Calculation")  

        self.title_label = ttk.Label(root, text="VAT", font=("Arial", 20))  
        self.title_label.pack(pady=10)

        self.price_label = ttk.Label(root, text="Enter the price", font=("Arial", 20))
        self.price_label.pack(pady=10)
        self.entry_price = Entry(root) 
        self.entry_price.pack(pady=10)  # Adds vertical padding

        self.vat_label = ttk.Label(root, text="Enter the VAT percentage", font=("Arial", 20))
        self.vat_label.pack(pady=10)
        self.entry_vat = Entry(root) 
        self.entry_vat.pack(pady=10)

        self.button = ttk.Button(root, text="Generate vat", command=self.generate_iva)
        self.button.pack(pady=10)

        self.result = ttk.Label(root, text="", font=("Arial", 14))
        self.result.pack(pady=10)

    def generate_iva(self):
        """
        Description: Calculates the final price, with a default VAT of 21%
        Args:
            entry_price (float): The price of the product.
            entry_vat (float): The VAT percentage. If not provided, defaults to 21%.
        
        Returns:
            float: The final price including VAT.
        
        Raises:
            Exception: If the input values are not valid numbers.
        """
        
        if(self.entry_vat.get()):
            try:
                price = float(self.entry_price.get())
                vat = float(self.entry_vat.get())
                # join the multiplication results into a single string
                final_price = price + (price * vat / 100)
                # Display the result in the label
                self.result.config(text=f"Final Price: {final_price:.2f}")
            except ValueError:
                self.result.config(text="Please enter a valid number.")
        else:
            try:
                price = float(self.entry_price.get())
                vat = 21
                # join the multiplication results into a single string
                final_price = price + (price * vat / 100)
                # Display the result in the label
                self.result.config(text=f"Final Price: {final_price:.2f}")
            except ValueError:
                self.result.config(text="Please enter a valid number.")

# Create the main window
root = Tk()
app = VatCalculationApp(root)
root.mainloop()