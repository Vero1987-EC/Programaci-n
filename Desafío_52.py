
class Libro:
    """Clase Libro encapsulada con atributos privados y métodos de acceso explícitos."""

    def __init__(self, titulo, autor, isbn):
        self.__titulo = None
        self.__autor = None
        self.__isbn = None

        # Asignación a través de setters para ejecutar validaciones iniciales
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_isbn(isbn)

    # --- GETTER Y SETTER PARA TÍTULO ---
    def get_titulo(self):
        """Retorna el título privado del libro."""
        return self.__titulo

    def set_titulo(self, titulo):
        """Establece el título validando que sea una cadena no vacía."""
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("Error: El título debe ser una cadena de texto no vacía.")
        self.__titulo = titulo.strip()

    # --- GETTER Y SETTER PARA AUTOR ---
    def get_autor(self):
        """Retorna el autor privado del libro."""
        return self.__autor

    def set_autor(self, autor):
        """Establece el autor validando que sea una cadena no vacía."""
        if not isinstance(autor, str) or not autor.strip():
            raise ValueError("Error: El autor debe ser una cadena de texto no vacía.")
        self.__autor = autor.strip()

    # --- GETTER Y SETTER PARA ISBN ---
    def get_isbn(self):
        """Retorna el ISBN privado del libro."""
        return self.__isbn

    def set_isbn(self, isbn):
        """Establece el ISBN validando que sea una cadena no vacía."""
        if not isinstance(isbn, str) or not isbn.strip():
            raise ValueError("Error: El ISBN debe ser una cadena de texto no vacía.")
        self.__isbn = isbn.strip()

    def mostrar_detalle(self):
        """Muestra los detalles del libro."""
        print(f" Título: {self.get_titulo()}")
        print(f"   Autor:  {self.get_autor()}")
        print(f"   ISBN:   {self.get_isbn()}")


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 52: CLASE LIBRO ENCAPSULADA ---")
    print("-" * 60)

    # 1. Instanciación correcta
    libro1 = Libro("Cómo hacer que te pasen cosas buenas", "Marian Rojas Estapé", "978-84-670-5339-5")
    libro1.mostrar_detalle()

    print("-" * 60)
    # 2. Modificación vía setters
    libro1.set_titulo("Encuentra tu persona vitamina")
    print("Modificación exitosa con set_titulo():")
    print(f"Nuevo título (vía get_titulo): {libro1.get_titulo()}")

    # 3. Intento de acceso directo a atributo privado
    print("\nIntento de acceso directo a atributo privado self.__titulo:")
    try:
        print(libro1.__titulo)
    except AttributeError as e:
        print(f" Acceso bloqueado por Python: AttributeError ({e})")

    print("-" * 60)


if __name__ == "__main__":
    main()