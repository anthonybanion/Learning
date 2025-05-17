import tkinter as tk
from tkinter import ttk

def setup_styles():
    # Create a style for the calculator frame
    calculatorStyle = ttk.Style()
    calculatorStyle.configure("My.TFrame",
                font=("Arial", 16),
                padding=20,
                background="black",   
                foreground="white")

    # Create a style for the buttons
    buttonStyle = ttk.Style()
    buttonStyle.configure("My.TButton",
                font=("Arial", 16),
                padding=0.5,
                background="black",  
                foreground="white") 
    

    screenStyle = ttk.Style()
    screenStyle.configure("Calc.TLabel",
                    background="green",
                    foreground="white",
                    font=("Arial", 20),
                    borderwidth=1,
                    relief="solid")


    return calculatorStyle, buttonStyle, screenStyle