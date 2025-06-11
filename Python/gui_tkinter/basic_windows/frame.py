# Description: Create a frame in a window
# File: frame.py
# Create Date: 05/11/2024
# Update Date: 11/04/2025

import tkinter as tk

window = tk.Tk()
window.title("My primary Frame")
window.geometry("600x400")
window.configure(bg="lightgreen")

frame1 = tk.Frame(window)
frame1.configure(width=300, height=300, bg="lightblue", bd=5)
frame1.pack()  

frame2 = tk.Frame(frame1)
frame2.configure(width=200, height=200, bg="red", bd=5)
frame2.pack()

boton1 = tk.Button(frame1, text="Hello word") 
boton1.pack()

labelframe = tk.LabelFrame(frame2, text="Primer Label", bg="white", padx=10, pady=10)
labelframe.configure(width=100, height=100)
labelframe.pack()

boton2 = tk.Button(labelframe, text="Hello world in LabelFrame") 
boton2.pack()

window.mainloop()