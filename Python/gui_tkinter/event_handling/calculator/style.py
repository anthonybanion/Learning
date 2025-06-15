"""
This module contains the styles for the calculator application.
 
File: style.py
Author: Anthony Bañon
Created: 2025-05-17
Last Updated: 2025-05-17
"""


import tkinter as tk
from tkinter import ttk

def setup_styles():
    # Create a style for the calculator frame
    calculatorStyle = ttk.Style()
    calculatorStyle.configure("TFrame",
                font=("Arial", 16),
                background="black",   
                foreground="white")

    # Create a style for the buttons
    buttonStyle = ttk.Style()
    buttonStyle.configure("TButton",
                font=("Arial", 14),
                padding=(4,4),
                background="black",  
                foreground="white",
                borderwidth=1,
                )
    
    buttonEnterStyle = ttk.Style()
    buttonEnterStyle.configure("Enter.TButton",
                font=("Arial", 14),
                padding=(4,4),
                background="red",  
                foreground="white",
                borderwidth=1,
                )

    screenStyle = ttk.Style()
    screenStyle.configure("TLabel",
                    background="green",
                    foreground="white",
                    font=("Arial", 20),
                    borderwidth=1,
                    relief="solid")


    return calculatorStyle, buttonStyle, screenStyle