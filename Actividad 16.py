from idlelib.autocomplete import TRY_A


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
        self.libros = {}
        self.usuarios = {}

    def agregar_usuario(self):
            carnet = input("Ingresar carnet del usuario: ")
            if carnet in self.usuarios:
                print("Ya existe un usuario con ese carnet.\n")
                return
            nombre = input("Ingresar nombre del usuario: ")
            carrera = input("Ingresar la carrera del Usuario: ")
            self.usuarios[carnet] = Usuarios(carnet, nombre, carrera)
            print("Usuario agregado.\n")

    def mostrar_usuario(self):
        if not self.usuarios:
            print("No hay usuarios registrados.\n")
            return

        print("\nLista de usuarios:")
        for i, usuario in enumerate(self.usuarios.values(), start=1):
            print(f"{i}. {usuario.mostrar()}")
        print()

    def eliminar_usuario(self):
        carnet_buscado = input("Ingresar el carnet del Usuario a eliminar: ")
        if carnet_buscado in self.usuarios:
            del self.usuarios[carnet_buscado]
            print("Usuario eliminado.\n")
        else:
            print("Usuario no encontrado.\n")

    def agregar_libro(self):
        titulo = input("Ingresar Título del Libro a agregar: ")
        autor = input("Ingresar autor del libro: ")
        año= input("Ingresar año de publicación del libro: ")
        codigo = input("Ingresar codigo del libro: ")
        if codigo in self.libros:
            print("Ya existe un libro con ese codigo.\n")
            return
        self.usuarios[codigo] = Libros(titulo, autor, año)
        print("Libro agregado.\n")

    def mostrar_libro(self):
        if not self.libros:
            print("No hay libros registrados.\n")
            return

        print("\nLista de libros:")
        for i, libro in enumerate(self.libros.values(), start=1):
            print(f"{i}. {libro.mostrar()}")
        print()

    def eliminar_libro(self):
        codigo_buscado = input("Ingresar el codigo del libro a eliminar: ")
        if codigo_buscado in self.libros:
            del self.libros[codigo_buscado]
            print("Libro eliminado.\n")
        else:
            print("Libro no encontrado.\n")

class Gestiones_Biblioteca:
    def prestamo(self):
        pass
    def devoluciones(self):
        pass

biblioteca = Biblioteca()
gestiones = Gestiones_Biblioteca()
def main():
    while True:
        try:
            op = int(0)
            print("1) Agregar Usuario")
            print("2) Eliminar Usuario")
            print("3) Mostrar Usuarios")
            print("4) Agregar Libro")
            print("5) Eliminar Libro")
            print("6) Mostrar Libros")
            print("7) Prestar Libro")
            print("8) Devolver Libro")
            print("9) Salir")
            op = int(input("Ingresar opcion: "))

            match(op):
                case 1:
                    biblioteca.agregar_usuario()
                case 2:
                    biblioteca.eliminar_usuario()
                case 3:
                    biblioteca.mostrar_usuario()
                case 4:
                    biblioteca.agregar_libro()
                case 5:
                    biblioteca.eliminar_libro()
                case 6:
                    biblioteca.mostrar_libro()
                case 7:
                    gestiones.prestamo()
                case 8:
                    gestiones.devoluciones()
                case 9:
                    print("Saliendo... ")
                    break
                case _:
                    print("Opcion no valida.\n")
        except:
            print("Hubo un Error")