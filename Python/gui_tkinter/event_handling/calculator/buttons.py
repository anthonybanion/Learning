# botones.py
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
            (".", 5, 0), ("0", 5, 1), ("e", 5, 2),("e", 5, 3),("=", 5, 4)
        ]
        for (text, row, col) in buttons:
            button = ttk.Button(self.parent, text=text, style="My.TButton",
                                command=lambda t=text: self.command_callback(t))
            button.grid(row=row, column=col, padx=0.5, pady=0.5, ipadx=20, ipady=20, sticky="nsew")