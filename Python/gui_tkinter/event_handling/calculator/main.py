

import tkinter as tk
from tkinter import ttk
from calculate import *
from Style import setup_styles
from buttons import Buttons
from screen import Screen

def main():
    root = tk.Tk()  # Create the main window
    root.geometry("594x717")  

    calculator = ttk.Frame(root, style="My.TFrame")
    calculator.pack(fill='both', expand='yes', )

    # Apply custom styles
    setup_styles()
    # Create a label to display the result
    screen = Screen(calculator)

    def al_pulsar(tecla):
        screen.update(tecla)

    buttons = Buttons(calculator, command_callback=al_pulsar)

    root.mainloop()

if __name__ == "__main__":
    main()