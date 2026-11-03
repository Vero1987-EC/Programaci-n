"""
Desafío 44: Sistemas con múltiples entidades interconectadas

"""

class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True


class Usuario:

    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo
        self.tiene_multa = False


class Prestamo:

    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario

    def registrar_prestamo(self):
        if not self.libro.disponible:
            print(f"Error: El libro '{self.libro.titulo}' no está disponible.")
            return False
        if self.usuario.tiene_multa:
            print(
                f"Error: El usuario {self.usuario.nombre} tiene multas pendientes."
            )
            return False

        self.libro.disponible = False
        print(
            f"Préstamo exitoso: '{self.libro.titulo}' asignado a"
            f" {self.usuario.nombre}."
        )
        return True


def main():
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
    usuario1 = Usuario("Verónica Etcheverry", "U101")

    prestamo1 = Prestamo(libro1, usuario1)
    prestamo1.registrar_prestamo()


if __name__ == "__main__":
    main()
    