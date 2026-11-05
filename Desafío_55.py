class Libro:
    """Clase Libro encapsulada."""

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
        return f"'{self.__titulo}'"


class Autor:
    """Clase Autor que encapsula su lista de libros."""

    def __init__(self, nombre, nacionalidad):
        self.__nombre = None
        self.__nacionalidad = None
        self.__libros = []  # Lista privada de libros

        self.nombre = nombre
        self.nacionalidad = nacionalidad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La nacionalidad no puede estar vacía.")
        self.__nacionalidad = valor.strip()

    def agregar_libro(self, libro):
        """Agrega un objeto Libro o título a la lista privada."""
        if isinstance(libro, Libro):
            self.__libros.append(libro)
        elif isinstance(libro, str) and libro.strip():
            self.__libros.append(Libro(libro, "S/N"))
        else:
            raise ValueError("El libro debe ser de clase Libro o un string no vacío.")

    def obtener_titulos_libros(self):
        """
        Método público que devuelve únicamente la lista de los títulos de los libros,
        respetando el encapsulamiento y sin exponer los objetos internos ni la lista privada.
        """
        titulos = []
        for elem in self.__libros:
            if isinstance(elem, Libro):
                titulos.append(elem.get_titulo())
            else:
                titulos.append(str(elem))
        return titulos


def obtener_titulos_de_autor(autor):
    """
    Función externa que toma un objeto Autor y devuelve una lista con los títulos.
    Garantiza el encapsulamiento al acceder únicamente mediante el método público
    del objeto Autor (autor.obtener_titulos_libros()).
    """
    if not isinstance(autor, Autor):
        raise TypeError("Error: El argumento debe ser una instancia de la clase Autor.")
    
    # Acceso estricto a través de la interfaz pública del objeto Autor
    return autor.obtener_titulos_libros()


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 55: OBTENER TÍTULOS CON ENCAPSULAMIENTO ---")
    print("-" * 65)

    # 1. Instanciación del autor
    autor1 = Autor("Marian Rojas Estapé", "Española")

    # 2. Agregamos libros
    l1 = Libro("Cómo hacer que te pasen cosas buenas", "978-84-670-5339-5")
    l2 = Libro("Encuentra tu persona vitamina", "978-84-670-6290-8")

    autor1.agregar_libro(l1)
    autor1.agregar_libro(l2)

    # 3. Invocación de la función externa
    titulos = obtener_titulos_de_autor(autor1)

    print(f"Autor: {autor1.nombre}")
    print("Títulos obtenidos mediante la función externa:")
    for idx, titulo in enumerate(titulos, 1):
        print(f"  {idx}. {titulo}")

    print("-" * 65)


if __name__ == "__main__":
    main()