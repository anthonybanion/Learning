# Description: Enter a number from the keyboard
#  and generate the multiplication table
# File: multiplicationTable.py
# Create Date: 05/11/2024



from tkinter import *
from tkinter import ttk
root = Tk()
windows =ttk.Label(root, text="Multiplication Table", font=("Arial", 20))
windows.pack(pady=10)

entry = Entry(root)
entry.pack(pady=10)

def generate_table():
    try:
        number = int(entry.get())
        table = "\n".join([f"{number} x {i} = {number * i}" for i in range(1, 13)])
        result.config(text=table)
    except ValueError:
        result.config(text="Please enter a valid number.")

button = ttk.Button(root, text="Generate", command=generate_table)
button.pack(pady=10)
result = ttk.Label(root, text="", font=("Arial", 14))
result.pack(pady=10)


root.mainloop()