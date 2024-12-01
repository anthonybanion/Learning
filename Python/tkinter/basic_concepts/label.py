#Briefa: Create a label in a window
#Date: 05/11/2024
#version: 1.0

import tkinter as tk

ventana = tk.Tk()
ventana.title("My primer Fame")
ventana.geometry("600x400")
ventana.configure(bg="lightgreen")

etiqueta = tk.Label(ventana,text="Hoy es un dia para hacer las cosas bien")
etiqueta.config(fg="blue", bg="yellow", font=("Arial", 12, "bold"))
etiqueta.pack()

ventana.mainloop()