"""
Description: Application that displays "Hello World!" and a Quit button.

File: helloWorld.py
Author: Anthony Bañon
Created: 2025-05-17
Last Updated: 2025-05-17
"""


from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)  # Create a frame with padding
frm.grid()  # Add the frame to the grid
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()