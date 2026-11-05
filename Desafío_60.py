class Autor:
    """Clase base que representa a un Autor."""

    def __init__(self, nombre, **kwargs):
        super().__init__(**kwargs)
        self.__nombre = None
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()


class Escritor(Autor):
    """Subclase que representa a un Escritor de un género específico."""

    def __init__(self, genero, **kwargs):
        super().__init__(**kwargs)
        self.__genero = None
        self.genero = genero

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El género no puede estar vacío.")
        self.__genero = valor.strip()


class Academico:
    """Clase base que representa a un Académico universitario."""

    def __init__(self, universidad, **kwargs):
        super().__init__(**kwargs)
        self.__universidad = None
        self.universidad = universidad

    @property
    def universidad(self):
        return self.__universidad

    @universidad.setter
    def universidad(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La universidad no puede estar vacía.")
        self.__universidad = valor.strip()


class EscritorAcademico(Escritor, Academico):
    """
    Subclase con Herencia Múltiple (Escritor y Academico).
    Utiliza super() para la inicialización en cadena (MRO) y añade
    el método publicar_articulo().
    """

    def __init__(self, nombre, genero, universidad):
        # Invocación cooperativa con super() y paso de argumentos clave
        super().__init__(nombre=nombre, genero=genero, universidad=universidad)
        self.__articulos = []

    def publicar_articulo(self, titulo_articulo, revista):
        """Método adicional exclusivo para publicar artículos académicos."""
        articulo = f"'{titulo_articulo.strip()}' en {revista.strip()}"
        self.__articulos.append(articulo)
        print(f" Artículo publicado por {self.nombre}: {articulo}")

    def obtener_articulos(self):
        return list(self.__articulos)

    def mostrar_perfil(self):
        """Muestra el perfil completo integrando todos los atributos heredados."""
        print(f"\n=======================================================")
        print(f" PERFIL DE ESCRITOR ACADÉMICO")
        print(f"=======================================================")
        print(f"Nombre:      {self.nombre}")
        print(f"Género:      {self.genero}")
        print(f"Universidad: {self.universidad}")
        print(f"Artículos:   {len(self.__articulos)} publicado(s)")
        if self.__articulos:
            for idx, art in enumerate(self.__articulos, 1):
                print(f"   {idx}. {art}")
        print(f"=======================================================\n")


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 60: ESCRITOR ACADÉMICO (HERENCIA MÚLTIPLE) ---")
    print("-" * 65)

    # Instanciación utilizando super()
    escritor_acad = EscritorAcademico(
        nombre="Umberto Eco",
        genero="Ensayo y Semiótica",
        universidad="Universidad de Bolonia"
    )

    # Invocación del método especializado para publicar artículos
    escritor_acad.publicar_articulo("La estructura ausente", "Revista de Semiótica y Filosofía")
    escritor_acad.publicar_articulo("Semiótica y Filosofía del Lenguaje", "Boletín Académico de Bolonia")

    # Mostrar perfil completo
    escritor_acad.mostrar_perfil()


if __name__ == "__main__":
    main()