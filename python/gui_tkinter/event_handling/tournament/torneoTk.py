import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from torneo import *


def main():
    ventana = tk.Tk()
    ventana.title("Torneo de futbol")
    ventana.geometry("600x400")
    notebook = ttk.Notebook(ventana)   #notebook es la solapa
    notebook.pack(fill='both', expand='yes')
    tab_ver_equipos = ttk.Frame(notebook)  #  son cada solapa teniendo creado el notebook
    notebook.add(tab_ver_equipos, text="Ver Equipos")

    def mostrar_equipos():
        columna = ("Nombre", "Ciudad", "Jugadores")
        lista_equipos = ttk.Treeview(tab_ver_equipos, columns=columna, show='headings')
        lista_equipos.pack(pady=10, fill='both', expand=True)
        for col in columna:
            lista_equipos.heading(col, text=col)
            lista_equipos.column(col, width=100, anchor='center')
        
        equipos = listar_equipos()

        for equipo in equipos:
            lista_equipos.insert("", tk.END, values=(equipo.nombre, equipo.ciudad, equipo.jugadores))
   
    mostrar_equipos()
    ventana.mainloop()
main()









