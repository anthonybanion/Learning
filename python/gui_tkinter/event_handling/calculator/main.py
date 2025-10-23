"""
Main application for the calculator.

File: main.py
Author: Anthony Bañon
Created: 2025-05-17
Last Updated: 2025-05-17
"""


import tkinter as tk
from tkinter import ttk
from calculate import *
from style import setup_styles
from buttons import Buttons
from screen import Screen

def main():
    root = tk.Tk()  # Create the main window
    root.geometry("594x717")  

    calculator = ttk.Frame(root, style="TFrame")
    calculator.pack(fill='both', expand='yes', )

    # Apply custom styles
    setup_styles()

    # Create a label to display the result
    screen = Screen(calculator)

    def al_pulsar(tecla):
        screen.update(tecla)

    buttons = Buttons(calculator, command_callback=al_pulsar)
    enterButton = buttons.create_button_enter()

    root.mainloop()

if __name__ == "__main__":
    main()