class Libro:
    """Clase base encapsulada Libro."""

    def __init__(self, titulo, autor):
        self.__titulo = None
        self.__autor = None

        self.titulo = titulo
        self.autor = autor

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

    def mostrar_informacion(self):
        """Muestra los datos básicos del libro."""
        print(f" Título: {self.titulo}")
        print(f"   Autor:  {self.autor}")


class LibroEspecializado(Libro):
    """
    Subclase LibroEspecializado que hereda de Libro.
    Añade atributos: 'campo_estudio' y 'nivel_especializacion'.
    """

    NIVELES_VALIDOS = ("básico", "intermedio", "avanzado")

    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
        super().__init__(titulo, autor)
        self.__campo_estudio = None
        self.__nivel_especializacion = None

        self.campo_estudio = campo_estudio
        self.nivel_especializacion = nivel_especializacion

    @property
    def campo_estudio(self):
        return self.__campo_estudio

    @campo_estudio.setter
    def campo_estudio(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El campo de estudio no puede estar vacío.")
        self.__campo_estudio = valor.strip()

    @property
    def nivel_especializacion(self):
        return self.__nivel_especializacion

    @nivel_especializacion.setter
    def nivel_especializacion(self, valor):
        if not isinstance(valor, str) or valor.strip().lower() not in self.NIVELES_VALIDOS:
            raise ValueError(
                f"Nivel no válido. Debe ser uno de los siguientes: {', '.join(self.NIVELES_VALIDOS)}."
            )
        self.__nivel_especializacion = valor.strip().lower()

    def mostrar_informacion(self):
        """Sobrescribe el método mostrar_informacion de Libro."""
        super().mostrar_informacion()
        print(f"   Campo de Estudio: {self.campo_estudio}")
        print(f"   Nivel:            {self.nivel_especializacion.capitalize()}")


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 64: LIBRO ESPECIALIZADO ---")
    print("-" * 65)

    # 1. Instanciación de un LibroEspecializado
    libro_esp = LibroEspecializado(
        titulo="Inteligencia Artificial: Un Enfoque Moderno",
        autor="Stuart Russell y Peter Norvig",
        campo_estudio="Ciencias de la Computación / IA",
        nivel_especializacion="avanzado"
    )

    # 2. Mostrar la información del libro especializado
    print("Ficha de Libro Especializado:")
    libro_esp.mostrar_informacion()

    print("-" * 65)

    # 3. Validación del nivel de especialización
    print("Intento de asignar un nivel de especialización inválido:")
    try:
        libro_esp.nivel_especializacion = "experto"
    except ValueError as e:
        print(f" Validación activada: {e}")

    print("-" * 65)


if __name__ == "__main__":
    main()