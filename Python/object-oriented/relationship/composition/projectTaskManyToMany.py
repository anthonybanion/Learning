#Brief: Project and Task
#Detail: The relationship between the two classes is many-to-many, where each project has many tasks and each task belongs to a project.
#Date: 06/11/2024
#Version: 1.0



class Tarea:
    def __init__(self, descripcion, proyecto):
        self.descripcion = descripcion
        self.proyecto = proyecto  # Composición: la tarea depende del proyecto
        print(f"Tarea '{self.descripcion}' creada y asociada al proyecto '{self.proyecto.nombre}'.")

    def mostrar(self):
        print(f"Tarea: {self.descripcion}, Proyecto: {self.proyecto.nombre}")
    
    def __del__(self):
        print(f"La tarea '{self.descripcion}' ha sido destruida porque el proyecto '{self.proyecto.nombre}' fue destruido.")


class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []  # Lista de tareas que pertenecen a este proyecto
        print(f"Proyecto '{self.nombre}' creado.")
    
    def agregar_tarea(self, descripcion):
        # Cada tarea pertenece de manera compuesta a este proyecto
        tarea = Tarea(descripcion, self)
        self.tareas.append(tarea)
    
    def mostrar_tareas(self):
        print(f"Las tareas del proyecto '{self.nombre}' son:")
        for tarea in self.tareas:
            tarea.mostrar()
    
    def __del__(self):
        print(f"El proyecto '{self.nombre}' ha sido destruido. Las tareas también se destruyen.")
        # Cuando el proyecto se destruye, las tareas asociadas también se destruyen.
        for tarea in self.tareas:
            del tarea


# Creación de proyectos con tareas (Muchos a Muchos en Composición)
proyecto1 = Proyecto("Desarrollo de Software")
proyecto2 = Proyecto("Lanzamiento de Producto")

# Agregar tareas a los proyectos
proyecto1.agregar_tarea("Definir requisitos")
proyecto1.agregar_tarea("Desarrollar código")

proyecto2.agregar_tarea("Desarrollar código")
proyecto2.agregar_tarea("Pruebas")

# Mostrar tareas de cada proyecto
proyecto1.mostrar_tareas()
proyecto2.mostrar_tareas()

# Eliminar proyectos (esto destruirá las tareas también)
del proyecto1
del proyecto2
