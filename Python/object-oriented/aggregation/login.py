class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password

    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}"

class Login:
    def __init__(self):
        self.usuarios = []

    def crear_usuario(self, nombre, email, password): #Creacion del usuario
        nuevo_usuario = Usuario(nombre, email, password)
        self.usuarios.append(nuevo_usuario)
        print("Usuario creado correctamente")

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios creados.")
            return
        print("Usuarios creados:")
        for usuario in self.usuarios:
            print(usuario)

    def login(self, email, password):
        for usuario in self.usuarios: #LLama a la lista de usuarios dentro de la clase Login
            if usuario.email == email and usuario.password == password: #Valida que las entradas sean iguales
                print("Login correcto")
                return True
        print("Email o contraseña incorrectos")
        return False



login = Login() #Se asigna la clase Login a la variable login para que no de error diciendo falta el argumento
                #self, si no lo paso, va a decir que en el paso de argumentos falta uno, que sería self.


login.crear_usuario("Juan", "juan@perez.com", "123456") #Aca llamo desde la variable login, que es una asignacion
                                                        #de la clase Login()
login.crear_usuario("Roberta", "roberta@mail.com", "abcdef")


login.mostrar_usuarios()


login.login("juan@perez.com", "123456")
login.login("juan@perez.com", "estanoeslacontraseña")

login.login("roberta@mail.com", "abcdef")
login.login("roberta@mail.com", "contraseñainvalida")
