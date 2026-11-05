class Libro:
    """Clase base encapsulada que representa un Libro genérico."""

    def __init__(self, titulo, autor, isbn):
        self.__titulo = None
        self.__autor = None
        self.__isbn = None

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El título no puede estar vacío.")
        self.__titulo = valor.strip()

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El autor no puede estar vacío.")
        self.__autor = valor.strip()

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El ISBN no puede estar vacío.")
        self.__isbn = valor.strip()

    def mostrar_detalle(self):
        """Muestra la información técnica básica del libro."""
        print(f" Título: {self.titulo}")
        print(f"   Autor:  {self.autor}")
        print(f"   ISBN:   {self.isbn}")


class LibroDigital(Libro):
    """
    Subclase LibroDigital que hereda de Libro.
    Añade atributos: formato (PDF, EPUB) y tamano_archivo (en MB).
    """

    def __init__(self, titulo, autor, isbn, formato, tamano_archivo):
        super().__init__(titulo, autor, isbn)
        self.__formato = None
        self.__tamano_archivo = None

        self.formato = formato
        self.tamano_archivo = tamano_archivo

    @property
    def formato(self):
        return self.__formato

    @formato.setter
    def formato(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El formato debe ser una cadena no vacía (ej. PDF, EPUB).")
        self.__formato = valor.strip().upper()

    @property
    def tamano_archivo(self):
        return self.__tamano_archivo

    @tamano_archivo.setter
    def tamano_archivo(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El tamaño de archivo debe ser un número positivo en MB.")
        self.__tamano_archivo = float(valor)

    def mostrar_detalle(self):
        """Sobrescribe mostrar_detalle para incorporar los datos digitales."""
        super().mostrar_detalle()
        print(f"   Formato: {self.formato} | Tamaño: {self.tamano_archivo:.2f} MB")


class EBook(LibroDigital):
    """
    Subclase EBook que hereda de LibroDigital.
    Sobrescribe el método mostrar_detalle para mostrar información específica
    como el enlace de descarga.
    """

    def __init__(self, titulo, autor, isbn, formato, tamano_archivo, enlace_descarga):
        super().__init__(titulo, autor, isbn, formato, tamano_archivo)
        self.__enlace_descarga = None
        self.enlace_descarga = enlace_descarga

    @property
    def enlace_descarga(self):
        return self.__enlace_descarga

    @enlace_descarga.setter
    def enlace_descarga(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El enlace de descarga no puede estar vacío.")
        self.__enlace_descarga = valor.strip()

    def mostrar_detalle(self):
        """
        Sobrescribe mostrar_detalle para incluir la información específica de EBook
        y su enlace de descarga.
        """
        print("\n" + "=" * 65)
        print(" FICHA TÉCNICA DE EBOOK (MÉTODO SOBREESCRITO)")
        print("=" * 65)
        super().mostrar_detalle()
        print(f"    Enlace de Descarga: {self.enlace_descarga}")
        print("=" * 65 + "\n")


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 59: LIBRO DIGITAL Y EBOOK (HERENCIA) ---")
    print("-" * 65)

    # 1. Instanciación de un LibroDigital
    libro_digital = LibroDigital(
        titulo="Cómo hacer que te pasen cosas buenas",
        autor="Marian Rojas Estapé",
        isbn="978-84-670-5339-5",
        formato="PDF",
        tamano_archivo=4.5
    )
    print("1. Objeto LibroDigital:")
    libro_digital.mostrar_detalle()

    print("-" * 65)
    # 2. Instanciación de un EBook
    ebook = EBook(
        titulo="Encuentra tu persona vitamina",
        autor="Marian Rojas Estapé",
        isbn="978-84-670-6290-8",
        formato="EPUB",
        tamano_archivo=2.8,
        enlace_descarga="descargas.biblioteca.org/ebooks/vitamina_9788467062908.epub"
    )

    print("2. Objeto EBook (Método Sobrescrito):")
    ebook.mostrar_detalle()


if __name__ == "__main__":
    main()