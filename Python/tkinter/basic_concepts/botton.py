#Briefa: Create a button in a window
#Date: 05/11/2024
#version: 1.0

import tkinter as tk

ventana = tk.Tk()
ventana.title("My primer Fame")
ventana.geometry("600x400")

boton = tk.Button(ventana, text="Presionar")
boton.config(fg="white", bg="green", font=("Arial", 14))
boton.pack()

def boton_presionado():
    print("Boton presionado")
boton.config(command=boton_presionado)

ventana.mainloop()