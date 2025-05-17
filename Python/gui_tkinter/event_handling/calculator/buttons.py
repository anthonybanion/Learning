"""
This module creates the buttons for the calculator interface.

File: buttons.py
Author: Anthony Bañon
Created: 2025-05-17
Last Updated: 2025-05-17
"""


import tkinter as tk
from tkinter import ttk

class Buttons:
    def __init__(self, parent, command_callback=None):
        self.parent = parent
        self.command_callback = command_callback or (lambda x: None)
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("m²", 1, 0),("m³", 1, 1), ("△", 1, 2),("□", 1, 3),("◯", 1, 4),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),("x²", 2, 3),("x³", 2, 4),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),("-", 3, 3),("%", 3, 4),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),("+", 4, 3),("*", 4, 4),
            (".", 5, 0), ("0", 5, 1),("=", 5, 4)
        ]
        for (text, row, col) in buttons:
            button = ttk.Button(self.parent, text=text, style="TButton",
                                command=lambda t=text: self.command_callback(t))
            button.grid(row=row, column=col, padx=2.1, pady=2.1, sticky="nsew")

    def create_button_enter(self): 
        button = ttk.Button(self.parent, text="Enter", style="Enter.TButton",
                            command=lambda t="Enter": self.command_callback(t))
        button.grid(row=5, column=2, columnspan=2, padx=2.1, pady=2.1, sticky="nsew")