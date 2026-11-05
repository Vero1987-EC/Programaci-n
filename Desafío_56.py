
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
    """Clase Autor que encapsula su lista de libros y estado interno."""

    def __init__(self, nombre, nacionalidad):
        self.__nombre = None
        self.__nacionalidad = None
        self.__libros = []

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
        """Agrega un libro a la colección privada."""
        if isinstance(libro, Libro):
            self.__libros.append(libro)
        elif isinstance(libro, str) and libro.strip():
            self.__libros.append(Libro(libro, "S/N"))
        else:
            raise ValueError("El libro debe ser un objeto Libro o una cadena no vacía.")

    def cantidad_libros(self):
        """
        Método público de consulta encapsulada que retorna la cantidad de obras publicadas.
        """
        return len(self.__libros)

    def obtener_titulos_libros(self):
        """Devuelve una lista de los títulos respetando el encapsulamiento."""
        return [l.get_titulo() if isinstance(l, Libro) else str(l) for l in self.__libros]


def obtener_autor_mas_prolifico(lista_autores):
    """
    Función externa que recibe una lista de objetos Autor y retorna el objeto Autor
    con la mayor cantidad de libros publicados.
    Garantiza el encapsulamiento al consultar la información exclusivamente a través
    del método público autor.cantidad_libros().
    """
    if not lista_autores:
        return None

    # Filtrar solo instancias válidas de la clase Autor
    autores_validos = [a for a in lista_autores if isinstance(a, Autor)]
    if not autores_validos:
        raise ValueError("La lista no contiene objetos válidos de la clase Autor.")

    # Búsqueda del autor con el máximo número de libros utilizando encapsulamiento
    autor_maximo = max(autores_validos, key=lambda autor: autor.cantidad_libros())
    return autor_maximo


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 56: AUTOR CON MÁS LIBROS ---")
    print("-" * 65)

    # 1. Creación de autores
    autor1 = Autor("Marian Rojas Estapé", "Española")
    autor2 = Autor("Lorena Pronsky", "Argentina")
    autor3 = Autor("Gabriel García Márquez", "Colombiano")

    # 2. Carga de libros
    autor1.agregar_libro("Cómo hacer que te pasen cosas buenas")
    autor1.agregar_libro("Encuentra tu persona vitamina")

    autor2.agregar_libro("Cúrame")
    autor2.agregar_libro("Despierta")
    autor2.agregar_libro("Rota se camina igual")  # 3 libros

    autor3.agregar_libro("Cien años de soledad")

    # 3. Lista de autores
    nomina_autores = [autor1, autor2, autor3]

    # 4. Invocación de la función de búsqueda
    prolifico = obtener_autor_mas_prolifico(nomina_autores)

    print("Resultados de la nómina:")
    for a in nomina_autores:
        print(f"   • {a.nombre}: {a.cantidad_libros()} libro(s) registrado(s).")

    print("-" * 65)
    print(f" El autor con mayor número de libros es: {prolifico.nombre}")
    print(f"   Nacionalidad: {prolifico.nacionalidad}")
    print(f"   Total de obras: {prolifico.cantidad_libros()}")
    print(f"   Títulos: {', '.join(prolifico.obtener_titulos_libros())}")
    print("-" * 65)


if __name__ == "__main__":
    main()
