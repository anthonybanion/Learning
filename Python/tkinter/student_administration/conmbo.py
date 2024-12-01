import tkinter as tk
from tkinter import ttk

def mostrar_seleccion():
    # Obtener el valor seleccionado
    seleccion = combo.get()
    print("Año de cursada seleccionado:", seleccion)

root = tk.Tk()

# Etiqueta para el Combobox
etiqueta = tk.Label(root, text="Selecciona el Año de Cursada:")
etiqueta.pack(pady=10)

# Crear el Combobox con los años de cursada
años = ['Año 1', 'Año 2', 'Año 3']
combo = ttk.Combobox(root, values=años)
combo.pack(pady=10)

# Botón para mostrar la selección
boton = tk.Button(root, text="Mostrar Selección", command=mostrar_seleccion)
boton.pack(pady=10)

root.mainloop()
