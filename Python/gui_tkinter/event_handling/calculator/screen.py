# pantalla.py
from tkinter import ttk
from Style import setup_styles

class Screen:
    def __init__(self, parent):
        self.label = ttk.Label(parent,text="Calculator", style="Calc.TLabel")
        self.label.grid(row=0, column=0, columnspan=5, pady=10, sticky="nsew")                 

    def update(self, text):
        self.label.config(text=text)
