#Briefa: Create a CRUD in a window with Tkinter
#Date: 05/11/2024
#version: 1.0

import tkinter as tk
from tkinter import ttk #todos los botones de Tkinter
#from crud import *  #importamos todas las funciones
from studentAdministration import listar_alumnos, crear_alumnos, buscar_alumnos, editar_alumnos, eliminar_alumnos  #importamos las funciones 
from tkinter import messagebox

def main():
    ventana = tk.Tk()
    ventana.title("CRUD")
    ventana.geometry("600x400")
    
    notebook = ttk.Notebook(ventana)   #notebook es la solapa
    notebook.pack(fill='both', expand='yes')  # se expande en toda la ventana

    tab_ver_alumnos = ttk.Frame(notebook)  #  son cada solapa teniendo creado el notebook
    notebook.add(tab_ver_alumnos, text="Ver Alumnos")
    tab_ads_alumno = ttk.Frame(notebook)
    notebook.add(tab_ads_alumno, text="Agregar Alumno")
    tab_buscar_alumno = ttk.Frame(notebook)
    notebook.add(tab_buscar_alumno, text="Buscar Alumno")

    # def mostrar_alumnos():
    #     alumnos = listar_alumnos()
    #     lista_alumnos=tk.Listbox(tab_ver_alumnos)  #lista de alumnos
    #     lista_alumnos.pack(fill='both', expand='yes')
    #     cabecera = tk.Label(tab_ver_alumnos, text="Lista de Alumnos")  #cabecera de la lista 
    #     lista_alumnos.insert(tk.END, "ID Nombre Apellido DNI")
    #     for alumno in alumnos:  #recorremos la lista de alumnos
    #         lista_alumnos.insert(tk.END, f'{alumno[0]} {alumno[1]} {alumno[2]} {alumno[3]}')
        
    #     return lista_alumnos

    def mostrar_alumnos():
        columna = ("ID", "Nombre", "Apellido", "DNI")  #cabezera de la tabla
        lista_alumnos=ttk.Treeview(tab_ver_alumnos, columns=columna, show='headings')  #creamos la tabla
        lista_alumnos.pack(pady=10, fill='both', expand=True)  #se expande en toda la ventana
        for col in columna:  #Configurar las cabeceras de las columnas:
            lista_alumnos.heading(col, text=col)  #establece el texto que aparecerá como cabecera de cada columna
            lista_alumnos.column(col, width=100, anchor='center')  #establece el ancho de cada columna
        alumnos=listar_alumnos()  #llamamos a la funcion listar_alumnos
        for alumno in alumnos:
            lista_alumnos.insert("", tk.END, values=(alumno[0],alumno[1], alumno[2], alumno[3]))  #insertamos los valores en la tabla
    
        def actualizar_alumnos():
            for item in lista_alumnos.get_children():
                lista_alumnos.delete(item)  #elimina todos los elementos de la tabla
            alumnos = listar_alumnos()
            for alumno in alumnos:
                lista_alumnos.insert("", tk.END, values=(alumno[0],alumno[1], alumno[2], alumno[3]))
            tab_ads_alumno.after(1000, actualizar_alumnos)  #actualiza la tabla cada 1000 milisegundos
        
        actualizar_alumnos()

    
    def agregar_alumno():

        tk.Label(tab_ads_alumno, text="Nombre:").grid(pady=5, row=0, column=0)
        tk.Label(tab_ads_alumno, text="Apellido:").grid(pady=5, row=1, column=0)
        tk.Label(tab_ads_alumno, text="DNI:").grid(pady=5, row=2, column=0)

        entry_nombre = tk.Entry(tab_ads_alumno, width=40)
        entry_nombre.grid(padx=5, row=0, column=1)

        entry_apellido = tk.Entry(tab_ads_alumno, width=40)
        entry_apellido.grid(padx=5, row=1, column=1)

        entry_dni = tk.Entry(tab_ads_alumno, width=40)
        entry_dni.grid(padx=5, row=2, column=1)

        def guardar_alumno():
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            dni = entry_dni.get()
             # Verificar que todos los campos estén llenos
            if nombre and apellido and dni:
                # Generar un ID único
                id = len(listar_alumnos()) + 1

                # Intentar insertar en la base de datos
                try:
                    crear_alumnos(id, nombre, apellido, dni)  # Asegúrate de pasar todos los argumentos
                    messagebox.showinfo("Éxito", "Alumno agregado correctamente.")
                    entry_nombre.delete(0, tk.END)
                    entry_apellido.delete(0, tk.END)
                    entry_dni.delete(0, tk.END)
                    notebook.tab(tab_ver_alumnos, state="normal")
                    notebook.select(tab_ver_alumnos)
                except Exception as e:
                    messagebox.showerror("Error", f"Ocurrió un error al agregar el alumno: {e}")



        tk.Button(tab_ads_alumno, text="Aceptar", width=50, command=guardar_alumno).grid(padx=10, pady=10, row=3, column=0, columnspan=2)

        

    def buscar_alumno():
    # Crear la interfaz para la búsqueda del alumno
        tk.Label(tab_buscar_alumno, text="ID:").grid(pady=5, row=0, column=0)
        id_entry = tk.Entry(tab_buscar_alumno, width=40)
        id_entry.grid(padx=5, row=0, column=1)
        
        # Función para realizar la búsqueda
        def buscar():
            def modificar_alumno():
                nombre = entry_nombre.get()
                apellido = entry_apellido.get()
                dni = entry_dni.get()
                if id and nombre:
                    try:
                        editar_alumnos(id, nombre, apellido, dni)
                        messagebox.showinfo("Éxito", "Alumno modificado correctamente.")
                        notebook.tab(tab_ver_alumnos, state="normal")
                        notebook.select(tab_ver_alumnos)
                    except Exception as e:
                        messagebox.showerror("Error", f"Ocurrió un error al modificar el alumno: {e}")

            def eliminar_alumno():
                if id:
                    try:
                        eliminar_alumnos(id)
                        messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
                        notebook.tab(tab_ver_alumnos, state="normal")
                        notebook.select(tab_ver_alumnos)
                    except Exception as e:
                        messagebox.showerror("Error", f"Ocurrió un error al eliminar el alumno: {e}")

            id = id_entry.get()
            # Verificar que el ID no esté vacío y sea un número positivo
            if not id.isdigit():
                messagebox.showerror("Error", "Por favor ingrese un ID válido (solo números).")
                return
            id = int(id)  # Convertir el ID a entero
            # Buscar el alumno usando la función buscar_alumnos(id)
            alumnos = buscar_alumnos(id)
            
            if alumnos:  # Si la lista de alumnos no está vacía
                # Mostrar los detalles del primer alumno encontrado
                alumno = alumnos[0]  # Suponiendo que la lista devuelve una tupla de (ID, Nombre, Apellido, DNI)
                #messagebox.showinfo("Alumno encontrado", f"ID: {alumno[0]}\nNombre: {alumno[1]}\nApellido: {alumno[2]}\nDNI: {alumno[3]}")
                tk.Label(tab_buscar_alumno, text="Nombre:").grid(pady=5, row=2, column=0)
                tk.Label(tab_buscar_alumno, text="Apellido:").grid(pady=5, row=3, column=0)
                tk.Label(tab_buscar_alumno, text="DNI:").grid(pady=5, row=4, column=0)

                entry_nombre = tk.Entry(tab_buscar_alumno, width=40)
                entry_nombre.insert(0, alumno[1])
                entry_nombre.grid(padx=5, row=2, column=1)

                entry_apellido = tk.Entry(tab_buscar_alumno, width=40)
                entry_apellido.insert(0, alumno[2])
                entry_apellido.grid(padx=5, row=3, column=1)

                entry_dni = tk.Entry(tab_buscar_alumno, width=40)
                entry_dni.insert(0, alumno[3])
                entry_dni.grid(padx=5, row=4, column=1)

                button_modify = tk.Button(tab_buscar_alumno, text="Modificar", width=50, command=modificar_alumno)
                button_modify.grid(padx=10, pady=10, row=5, column=0, columnspan=2)
                button_delete = tk.Button(tab_buscar_alumno, text="Eliminar", width=50, command=eliminar_alumno)
                button_delete.grid(padx=10, pady=10, row=6, column=0, columnspan=2)

            else:
                messagebox.showerror("Error", "El alumno no existe.")
            
            # Limpiar el campo de entrada después de la búsqueda
            id_entry.delete(0, tk.END)

        # Botón para activar la búsqueda
        button = tk.Button(tab_buscar_alumno, text="Buscar", width=50, command=buscar)
        button.grid(padx=10, pady=10, row=1, column=0, columnspan=2)


       
           







        #     tab_modificar_alumno.mainloop()
        # tab_ads_alumno.mainloop()
        # tab_buscar_alumno.mainloop()
        tab_ver_alumnos.mainloop()

   
    mostrar_alumnos()
    agregar_alumno()

    buscar_alumno()
    mostrar_alumnos()
    
    ventana.mainloop()


main()



