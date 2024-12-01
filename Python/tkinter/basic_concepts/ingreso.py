#Briefa: Create a calculator in a window
#Date: 05/11/2024
#version: 1.0

import tkinter as tk

def add_table():
    input_value = entry.get()
    try:
        input_value = int(input_value)
        result = input_value + 10
        label.config(text=f"Result: {result}")
    except ValueError:
        label.config(text="Invalid input!")

ventana = tk.Tk()
ventana.title("Tabla de Multiplicar")
ventana.geometry("300x200")

label = tk.Label(ventana, text="Enter a number:")
label.pack()

entry = tk.Entry(ventana)
entry.pack()

button = tk.Button(ventana, text="Ingrese un valor", command=add_table)
button.pack()

ventana.mainloop()