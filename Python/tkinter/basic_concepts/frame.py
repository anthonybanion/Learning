#Briefa: Create a frame in a window
#Date: 05/11/2024
#version: 1.0

import tkinter as tk

ventana = tk.Tk()
ventana.title("My primer Fame")
ventana.geometry("600x400")
ventana.configure(bg="lightgreen")

frame1 = tk.Frame(ventana)
frame1.configure(width=300, height=300, bg="lightblue", bd=5)
frame1.pack()

frame2 = tk.Frame(frame1)
frame2.configure(width=200, height=200, bg="red", bd=5)
frame2.pack()

boton1 = tk.Button(frame1, text="Hola") 
boton1.pack()

labelframe = tk.LabelFrame(frame2, text="Primer Label", bg="white", padx=10, pady=10)
labelframe.configure(width=100, height=100)
labelframe.pack()

boton2 = tk.Button(labelframe, text="Mundo") 
boton2.pack()

ventana.mainloop()