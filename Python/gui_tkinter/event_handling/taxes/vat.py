"""
Description: create a program that calculates VAT
 
File: iva.py
Author: Anthony Bañon
Created: 2025-04-23
Last Updated: 2025-04-23
"""



from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x400")  

title_label =ttk.Label(root, text="VAT", font=("Arial", 20))  
title_label.pack(pady=10)

price_label =ttk.Label(root, text="Enter the price", font=("Arial", 20))
price_label.pack(pady=10)
entry_price = Entry(root) 
entry_price.pack(pady=10)  # Adds vertical padding

vat_label =ttk.Label(root, text="Enter the VAT percentage", font=("Arial", 20))
vat_label.pack(pady=10)
entry_vat = Entry(root) 
entry_vat.pack(pady=10)  # Adds vertical padding

def generate_iva():
    """
    Description: calculates the final price, with a default VAT of 21%
    
    Args:
        entry_price (float): The price of the product.
        entry_vat (float): The VAT percentage. If not provided, defaults to 21%.
    
    Returns:
        str: The final price including VAT.
    
    Raises:
        ValueError: If the input is not a valid number.
        Exception: If the input is not a valid integer.
    """
    if(entry_vat.get()):
        try:
            price = float(entry_price.get())
            vat = float(entry_vat.get())
            # join the multiplication results into a single string
            final_price = price + (price * vat / 100)
            # Display the result in the label
            result.config(text=f"Final Price: {final_price:.2f}")
        except ValueError:
            result.config(text="Please enter a valid number.")
    else:
        try:
            price = float(entry_price.get())
            vat = 21
            # join the multiplication results into a single string
            final_price = price + (price * vat / 100)
            # Display the result in the label
            result.config(text=f"Final Price: {final_price:.2f}")
        except ValueError:
            result.config(text="Please enter a valid number.")
    
    
button = ttk.Button(root, text="Generate vat", command=generate_iva)
button.pack(pady=10)

# Create a label to display the result
result = ttk.Label(root, text="", font=("Arial", 14))
result.pack(pady=10)

root.mainloop()