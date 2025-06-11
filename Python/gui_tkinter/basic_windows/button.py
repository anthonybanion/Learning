# Description: Create a button in a window
# File: botton.py
# Create Date: 05/11/2024
# Update Date: 11/04/2025


import tkinter as tk

Windows = tk.Tk()
Windows.title("My primer Fame")
Windows.geometry("600x400")

boton = tk.Button(Windows, text="Enter", width=10, height=2)
boton.config(fg="white", bg="green", font=("Arial", 14))
boton.pack()

def pressButton():
    print("Button pressed")
boton.config(command=pressButton)

Windows.mainloop()