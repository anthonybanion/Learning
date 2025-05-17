"""
Description: The program calculates the area of ​​a circle and the volume 
            of a cylinder using the same function.
 
File: circuloArea.py
Author: Anthony Bañon
Created: 2025-04-23
Last Updated: 2025-05-17

"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Area")
root.geometry("400x350")   

tab_area = ttk.Frame(root)  
tab_area.pack(fill='both', expand='yes')


title_label =ttk.Label(tab_area, text="Area and volume", font=("Arial", 20))  
title_label.grid(pady=10, row=0, column=0)


    
radio_label =ttk.Label(tab_area, text="Enter the radius of the circle", font=("Arial", 20))
radio_label.grid(pady=10,padx=20, row=1, column=0)

entry_radio = tk.Entry(tab_area, width=40) 
entry_radio.grid(padx=10, row=2, column=0)

height_label =ttk.Label(tab_area, text="Enter the height of the cylinder", font=("Arial", 20))
height_label.grid(pady=10,padx=20, row=3, column=0)

entry_height = tk.Entry(tab_area, width=40) 
entry_height.grid(padx=10, row=4, column=0)

def calculates():   
     
    try:
        radio = float(entry_radio.get())
        height = float(entry_height.get())
        area = 3.14 * radio ** 2
        volume = area * height
        result.config(text=f"Area: {area:.2f}, Volume: {volume:.2f}")
    except ValueError:
        result.config(text="Please enter valid numbers.")

button = ttk.Button(tab_area, text="Calculate", command=calculates)
button.grid(pady=10, row=5, column=0)
result = ttk.Label(tab_area, text="", font=("Arial", 14))
result.grid(pady=5, row=6, column=0)  # Create a label to display the result


# Create a label to display the result
result = ttk.Label(tab_area, text="", font=("Arial", 14))
result.grid(pady=5, row=7, column=0)  # Create a label to display the result
calculates()
root.mainloop()