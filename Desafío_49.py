class Autor:

    def __init__(self, nombre, nacionalidad="Desconocida"):
        self.nombre = nombre.strip()
        self.nacionalidad = nacionalidad.strip()
        self.libros = []

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"


class Libro:

    def __init__(self, titulo, genero, isbn, autor=None):
        self.titulo = titulo.strip()
        self.genero = genero.strip()
        self.isbn = isbn.strip()
        self.autor = autor
        if autor and isinstance(autor, Autor):
            if self not in autor.libros:
                autor.libros.append(self)

    def __str__(self):
        nombre_autor = self.autor.nombre if self.autor else "Anónimo"
        return f"'{self.titulo}' - {nombre_autor} [{self.genero}] (ISBN: {self.isbn})"


class Biblioteca:
    """Clase contenedora que gestiona la colección de Autores y Libros."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.autores = []
        self.catalogo = {}  # Clave: ISBN -> Valor: Objeto Libro

    def registrar_libro(self, libro):
        if isinstance(libro, Libro):
            self.catalogo[libro.isbn] = libro
            if libro.autor and libro.autor not in self.autores:
                self.autores.append(libro.autor)
            print(
                f"📚 Libro '{libro.titulo}' ingresado al catálogo (ISBN:"
                f" {libro.isbn})."
            )

    def mostrar_catalogo_general(self):
        print("\n" + "=" * 50)
        print(f" CATÁLOGO GENERAL DE LA BIBLIOTECA: {self.nombre.upper()}")
        print("=" * 50)
        print(f"Total de autores: {len(self.autores)}")
        print(f"Total de títulos: {len(self.catalogo)}\n")
        for i, (isbn, libro) in enumerate(self.catalogo.items(), 1):
            print(f"  {i}. {libro}")
        print("=" * 50 + "\n")


def main():
    biblio = Biblioteca("Biblioteca Central")

    a1 = Autor("Marian Rojas Estapé", "Española")
    a2 = Autor("Lorena Pronsky", "Argentina")

    l1 = Libro(
        "Cómo hacer que te pasen cosas buenas",
        "Desarrollo Personal",
        "978-84-670-5339-5",
        a1,
    )
    l2 = Libro(
        "Encuentra tu persona vitamina",
        "Psicología",
        "978-84-670-6290-8",
        a1,
    )
    l3 = Libro("Cúrame", "Desarrollo Emocional", "978-950-49-7312-6", a2)

    biblio.registrar_libro(l1)
    biblio.registrar_libro(l2)
    biblio.registrar_libro(l3)

    biblio.mostrar_catalogo_general()


if __name__ == "__main__":
    main()