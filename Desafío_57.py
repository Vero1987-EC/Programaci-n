class Autor:
    """Clase base encapsulada que representa a un Autor."""

    def __init__(self, nombre, nacionalidad="Desconocida"):
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

    def agregar_libro(self, titulo):
        if isinstance(titulo, str) and titulo.strip():
            self.__libros.append(titulo.strip())
            print(f" Libro '{titulo.strip()}' agregado a {self.nombre}.")

    def obtener_libros(self):
        return list(self.__libros)

    def mostrar_informacion(self):
        print(f"Autor: {self.nombre} | Nacionalidad: {self.nacionalidad}")
        print(f"Libros registrados: {len(self.__libros)}")


class Poeta(Autor):
    """
    Subclase Poeta que hereda de Autor.
    Añade el atributo especializado 'tipo_poesia'.
    """

    def __init__(self, nombre, nacionalidad, tipo_poesia):
        # Invocación del constructor de la superclase
        super().__init__(nombre, nacionalidad)
        self.__tipo_poesia = None
        self.tipo_poesia = tipo_poesia

    @property
    def tipo_poesia(self):
        """Getter para el atributo tipo_poesia."""
        return self.__tipo_poesia

    @tipo_poesia.setter
    def tipo_poesia(self, valor):
        """Setter con validación para tipo_poesia."""
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El tipo de poesía debe ser una cadena no vacía.")
        self.__tipo_poesia = valor.strip()

    def recitar_poema(self, titulo_poema, estrofa):
        """Método especializado exclusivo de la clase Poeta."""
        print(f"\n {self.nombre} ({self.tipo_poesia}) recita '{titulo_poema}':")
        print(f"   \"{estrofa}\"")

    def mostrar_informacion(self):
        """Sobrescribe mostrar_informacion para incluir el tipo de poesía."""
        super().mostrar_informacion()
        print(f"Especialidad Poética: {self.tipo_poesia}")


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 57: CLASE POETA (HERENCIA) ---")
    print("-" * 65)

    # 1. Instanciación de un objeto Poeta
    poeta1 = Poeta("Mario Benedetti", "Uruguayo", "Poesía Lírica y Social")

    # 2. Reutilización de métodos heredados de Autor
    poeta1.agregar_libro("Inventario Uno")
    poeta1.agregar_libro("Poemas de la Oficina")

    # 3. Mostrar información completa (método sobrescrito)
    print("\nInformación del Poeta:")
    poeta1.mostrar_informacion()

    # 4. Uso del método especializado recitar_poema
    poeta1.recitar_poema(
        "Táctica y Estrategia",
        "Mi táctica es mirarte, aprender como sos, quererte como sos..."
    )

    print("-" * 65)


if __name__ == "__main__":
    main()