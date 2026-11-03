class Autor:

    def __init__(self, nombre, nacionalidad="Desconocida"):
        self.nombre = nombre.strip()
        self.nacionalidad = nacionalidad.strip()


class Libro:

    def __init__(self, titulo, genero, isbn, autor):
        self.titulo = titulo.strip()
        self.genero = genero.strip()
        self.isbn = isbn.strip()
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' por {self.autor.nombre} [ISBN: {self.isbn}]"


class SistemaBiblioteca:
    """Gestiona el catálogo e incluye métodos avanzados de búsqueda."""

    def __init__(self):
        self.libros = []
        self.autores = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        if libro.autor not in self.autores:
            self.autores.append(libro.autor)

    def buscar_libro_por_titulo(self, termino):
        """Busca libros cuyo título contenga el término (insensible a mayúsculas)."""
        termino_norm = termino.strip().lower()
        return [l for l in self.libros if termino_norm in l.titulo.lower()]

    def buscar_libro_por_isbn(self, isbn_buscado):
        """Busca un libro exacto por su ISBN."""
        isbn_norm = isbn_buscado.strip()
        return next((l for l in self.libros if l.isbn == isbn_norm), None)

    def buscar_libros_por_autor(self, nombre_autor):
        """Devuelve todos los libros de un autor específico."""
        termino_norm = nombre_autor.strip().lower()
        return [l for l in self.libros if termino_norm in l.autor.nombre.lower()]


def main():
    biblio = SistemaBiblioteca()

    a1 = Autor("Marian Rojas Estapé", "Española")
    a2 = Autor("Lorena Pronsky", "Argentina")
    a3 = Autor("Gabriel García Márquez", "Colombiano")

    biblio.agregar_libro(
        Libro(
            "Cómo hacer que te pasen cosas buenas",
            "Desarrollo Personal",
            "978-84-670-5339-5",
            a1,
        )
    )
    biblio.agregar_libro(
        Libro(
            "Encuentra tu persona vitamina",
            "Psicología",
            "978-84-670-6290-8",
            a1,
        )
    )
    biblio.agregar_libro(
        Libro("Cúrame", "Desarrollo Emocional", "978-950-49-7312-6", a2)
    )
    biblio.agregar_libro(
        Libro(
            "Cien años de soledad",
            "Realismo Mágico",
            "978-03-074-7472-8",
            a3,
        )
    )

    # 1. Búsqueda por término en título
    print("🔍 1. Buscando libros con el término 'persona':")
    for l in biblio.buscar_libro_por_titulo("persona"):
        print(f"   -> {l}")

    # 2. Búsqueda por autor
    print("\n🔍 2. Buscando libros del autor 'Marian':")
    for l in biblio.buscar_libros_por_autor("Marian"):
        print(f"   -> {l}")

    # 3. Búsqueda por ISBN
    print("\n🔍 3. Buscando libro por ISBN '978-950-49-7312-6':")
    res = biblio.buscar_libro_por_isbn("978-950-49-7312-6")
    print(f"   -> {res}")


if __name__ == "__main__":
    main()