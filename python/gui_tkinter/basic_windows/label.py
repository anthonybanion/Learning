#Create a label in a window
#File: label.py
#Created: 2024-11-05
#Last Updated: 2025-06-10
#version: 1.0

import tkinter as tk

root = tk.Tk()
root.title("My primary Frame")
root.geometry("600x400")
root.configure(bg="lightgreen")

label = tk.Label(root,text="Today is a day to do things right")
label.config(fg="blue", bg="yellow", font=("Arial", 12, "bold"))
label.pack()

root.mainloop()