from tkinter import *
from tkinter import ttk
from calculate import *

root = Tk()  # Create the main window
title_label =ttk.Label(root, text="Calculator", font=("Arial", 20))  
title_label.grid(padx=5, row=0, column=1)

button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=1, column=0)
button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=1, column=1)
button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=1, column=2)

button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=2, column=0)
button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=2, column=1)
button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=2, column=2)

button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=3, column=0)
button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=3, column=1)
button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=3, column=2)

button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=4, column=0)
button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=4, column=1)
button = ttk.Button(root, text="Generate")
button.grid(padx=5, row=4, column=2)
# Create a label to display the result
result = ttk.Label(root, text="", font=("Arial", 14))
result.grid(padx=5, row=7, column=1)


#buscar black new windows

root.mainloop()