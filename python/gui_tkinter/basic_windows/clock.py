#Briefa: Create a clock in a root
#Date: 05/11/2024
#version: 1.0

import time
import tkinter as tk

root = tk.Tk()
root.title("clock")

label = tk.Label(root, text="Hello World")
label.pack()

def updateTime():
    label.config(text=time.strftime("%H:%M:%S"))
    root.after(1000,updateTime)

updateTime()

root.mainloop()