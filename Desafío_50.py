class AutorCompleto:
    """Versión extendida de la clase Autor con atributos y métodos avanzados."""

    def __init__(
        self,
        nombre,
        nacionalidad="Desconocida",
        fecha_nacimiento=None,
        biografia="",
    ):
        self.nombre = nombre.strip()
        self.nacionalidad = nacionalidad.strip()
        self.fecha_nacimiento = fecha_nacimiento
        self.biografia = biografia.strip()
        self.activo = True
        self.premios = []
        self.libros = []

    def agregar_premio(self, premio):
        """Agrega un premio a la lista de reconocimientos del autor."""
        premio_limpio = premio.strip()
        if premio_limpio and premio_limpio not in self.premios:
            self.premios.append(premio_limpio)
            print(f" Premio '{premio_limpio}' otorgado a {self.nombre}.")

    def agregar_libro(self, titulo_libro):
        """Agrega el título de un libro a la colección del autor."""
        if titulo_libro not in self.libros:
            self.libros.append(titulo_libro)

    def total_obras_publicadas(self):
        """Devuelve el número total de obras escritas."""
        return len(self.libros)

    def mostrar_ficha_completa(self):
        """Imprime una ficha detallada con todos los atributos del autor."""
        print("\n" + "=" * 60)
        print(f"FICHA TÉCNICA DEL AUTOR: {self.nombre.upper()}")
        print("=" * 60)
        print(f"Nacionalidad:       {self.nacionalidad}")
        print(
            "Fecha Nacimiento:  "
            f" {self.fecha_nacimiento if self.fecha_nacimiento else 'No especificada'}"
        )
        print(
            "Estado Activo:     "
            f" {'Sí' if self.activo else 'Retirado / Inactivo'}"
        )
        print(f"Total de Obras:     {self.total_obras_publicadas()}")

        if self.biografia:
            print(f"\nBiografía: {self.biografia}")

        if self.premios:
            print("\nPremios y Reconocimientos:")
            for p in self.premios:
                print(f"  • {p}")

        if self.libros:
            print("\nLibros Registrados:")
            for l in self.libros:
                print(f"  • {l}")
        print("=" * 60 + "\n")


def main():
    autor = AutorCompleto(
        nombre="Marian Rojas Estapé",
        nacionalidad="Española",
        fecha_nacimiento="1983-11-02",
        biografia=(
            "Médica psiquiatra y escritora apasionada por la mente humana y las"
            " emociones."
        ),
    )

    autor.agregar_premio("Premio Novedal a la Divulgación Médica")
    autor.agregar_premio("Reconocimiento Best-Seller Internacional")

    autor.agregar_libro("Cómo hacer que te pasen cosas buenas")
    autor.agregar_libro("Encuentra tu persona vitamina")

    autor.mostrar_ficha_completa()


if __name__ == "__main__":
    main()