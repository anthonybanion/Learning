#Create first window
#File: window.py
#Created: 2024-11-05
#Last updated: 2025-06-10
#version: 1.0

import tkinter as tk

root = tk.Tk()
root.title("My primary root")
root.geometry("600x400+10+10")
root.minsize(400, 200)
root.maxsize(800, 600)
root.configure(bg="lightblue")

root.mainloop()
