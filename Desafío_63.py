class Autor:
    """Clase base Autor."""

    def __init__(self, nombre, nacionalidad="Desconocida"):
        self.__nombre = None
        self.__nacionalidad = None

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

    def biografia(self):
        """Método base de biografía."""
        return f"Autor: {self.nombre} ({self.nacionalidad})"


class Escritor(Autor):
    """Subclase Escritor que hereda de Autor."""

    def __init__(self, nombre, nacionalidad, genero_literario):
        super().__init__(nombre, nacionalidad)
        self.__genero_literario = None
        self.genero_literario = genero_literario

    @property
    def genero_literario(self):
        return self.__genero_literario

    @genero_literario.setter
    def genero_literario(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El género literario no puede estar vacío.")
        self.__genero_literario = valor.strip()

    def biografia(self):
        """
        Sobrescritura del método biografia().
        Combina la biografía de la clase base usando super().biografia()
        con los datos específicos de Escritor.
        """
        bio_base = super().biografia()
        return f"{bio_base} | Especialidad: Escritor de {self.genero_literario}"


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 63: MÉTODO BIOGRAFÍA EN AUTOR Y ESCRITOR ---")
    print("-" * 70)

    # 1. Instanciación de un objeto Escritor
    escritor1 = Escritor("Mario Benedetti", "Uruguayo", "Realismo Social y Poesía")

    # 2. Acceso a la biografía de la subclase Escritor (método sobrescrito)
    print("1. Acceso directo al método biografia() de la subclase Escritor:")
    print(f"    {escritor1.biografia()}")

    print("-" * 70)

    # 3. Acceso al método biografia() original de la superclase Autor desde la instancia Escritor
    print("2. Acceso explícito al método biografia() de la superclase Autor:")
    print(f"    {Autor.biografia(escritor1)}")

    print("-" * 70)


if __name__ == "__main__":
    main()