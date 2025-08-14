class Libros:
    def __init__(self, titulo, autor, año, codigo):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.codigo = codigo

class Usuarios:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera

    def mostrar_info(self):
        return f"Carnet: {self.carnet} - Nombre: {self.nombre} - Carrera: {self.carrera}"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = {}

    def agregar(self):
            carnet = input("Ingresar carnet del estudiante: ")
            if carnet in self.usuarios:
                print("Ya existe un estudiante con ese carnet.\n")
                return
            nombre = input("Ingresar nombre del estudiante: ")
            carrera = input("Ingresar edad del estudiante: ")
            self.usuarios[carnet] = Usuarios(carnet, nombre, carrera)
            print("Usuario agregado.\n")

    def mostrar(self):
        if not self.usuarios:
            print("No hay usuarios registrados.\n")
            return

        print("\nLista de usuarios:")
        for i, usuario in enumerate(self.usuarios.values(), start=1):
            print(f"{i}. {usuario.mostrar()}")
        print()

    def eliminar(self):
        carnet_buscado = input("Ingresar el carnet del estudiante a eliminar: ")
        if carnet_buscado in self.usuarios:
            del self.usuarios[carnet_buscado]
            print("Estudiante eliminado.\n")
        else:
            print("Estudiante no encontrado.\n")

class Gestiones_Biblioteca:
    pass