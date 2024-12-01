#Briefa: Create a window
#Date: 05/11/2024
#version: 1.0

import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("600x400+10+10")
ventana.minsize(400, 200)
ventana.maxsize(800, 600)
ventana.configure(bg="lightblue")

ventana.mainloop()
