#Briefa: Create a clock in a window
#Date: 05/11/2024
#version: 1.0

import time
import tkinter as tk

ventana = tk.Tk()
ventana.title("Reloj")

etiqueta = tk.Label(ventana, text="Hola Mundo")
etiqueta.pack()

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000,actualizar_hora)

actualizar_hora()

ventana.mainloop()