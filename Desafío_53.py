
class Libro:
    """Clase Libro encapsulada (utilizada para la relación con Autor)."""

    def __init__(self, titulo, isbn):
        self.__titulo = None
        self.__isbn = None
        self.set_titulo(titulo)
        self.set_isbn(isbn)

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("El título debe ser una cadena no vacía.")
        self.__titulo = titulo.strip()

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        if not isinstance(isbn, str) or not isbn.strip():
            raise ValueError("El ISBN debe ser una cadena no vacía.")
        self.__isbn = isbn.strip()

    def __str__(self):
        return f"'{self.__titulo}' (ISBN: {self.__isbn})"


class Autor:
    """Clase Autor con atributo privado __libros y método para agregar libros."""

    def __init__(self, nombre, nacionalidad):
        self.__nombre = None
        self.__nacionalidad = None
        self.__libros = []  # Colección privada de libros

        self.set_nombre(nombre)
        self.set_nacionalidad(nacionalidad)

    # --- GETTERS Y SETTERS BÁSICOS ---
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre.strip()

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        if not isinstance(nacionalidad, str) or not nacionalidad.strip():
            raise ValueError("La nacionalidad no puede estar vacía.")
        self.__nacionalidad = nacionalidad.strip()

    # --- GESTIÓN ENCAPSULADA DE LA LISTA DE LIBROS --- 
    def agregar_libro(self, libro):
        """
        Agrega un libro a la lista privada del autor.
        Acepta instancias de Libro o cadenas de texto.
        """
        if isinstance(libro, Libro):
            # Evita duplicados por ISBN
            if any(l.get_isbn() == libro.get_isbn() for l in self.__libros if isinstance(l, Libro)):
                print(f" El libro {libro} ya está registrado para este autor.")
                return False
            self.__libros.append(libro)
            print(f" Libro {libro} agregado con éxito a {self.__nombre}.")
            return True
        elif isinstance(libro, str) and libro.strip():
            titulo_limpio = libro.strip()
            if titulo_limpio in self.__libros:
                print(f" El libro '{titulo_limpio}' ya existe en la lista de {self.__nombre}.")
                return False
            self.__libros.append(titulo_limpio)
            print(f" Libro '{titulo_limpio}' agregado con éxito a {self.__nombre}.")
            return True
        else:
            raise ValueError("Error: El libro debe ser un objeto de la clase Libro o una cadena no vacía.")

    def get_libros(self):
        """
        Retorna una copia de la lista de libros para mantener el encapsulamiento.
        """
        return list(self.__libros)

    def mostrar_obras(self):
        """Muestra en pantalla el catálogo de libros del autor."""
        print(f"\n{'=' * 55}")
        print(f"AUTOR: {self.__nombre} ({self.__nacionalidad})")
        print("-" * 55)
        if not self.__libros:
            print(" No hay libros registrados en su catálogo.")
        else:
            print(" Catálogo de libros registrados:")
            for idx, libro in enumerate(self.__libros, 1):
                print(f"   {idx}. {libro}")
        print("=" * 55 + "\n")


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 53: AUTOR CON LISTA DE LIBROS ENCAPSULADA ---")

    # 1. Instanciación del autor
    autor = Autor("Marian Rojas Estapé", "Española")

    # 2. Creación y agregado de libros
    l1 = Libro("Cómo hacer que te pasen cosas buenas", "978-84-670-5339-5")
    l2 = Libro("Encuentra tu persona vitamina", "978-84-670-6290-8")

    autor.agregar_libro(l1)
    autor.agregar_libro(l2)

    # 3. Mostrar catálogo
    autor.mostrar_obras()

    # 4. Demostración de encapsulamiento
    copia_libros = autor.get_libros()
    copia_libros.clear()  # Modificamos la copia recibida

    print("Verificación de encapsulamiento tras borrar la lista devuelta por get_libros():")
    print(f"Cantidad de libros reales en el objeto Autor: {len(autor.get_libros())}")


if __name__ == "__main__":
    main()