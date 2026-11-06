
class Musico:
    """Clase base que representa a un Músico genérico."""

    def __init__(self, nombre):
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

    def instrumento(self):
        """Método base que será sobrescrito en las subclases."""
        return f"{self.nombre} toca un instrumento genérico."


class Guitarrista(Musico):
    """Subclase Guitarrista que hereda de Musico."""

    def __init__(self, nombre, tipo_guitarra="Eléctrica"):
        super().__init__(nombre)
        self.tipo_guitarra = tipo_guitarra

    def instrumento(self):
        """Sobrescritura del método instrumento()."""
        return f" {self.nombre} ejecuta la guitarra {self.tipo_guitarra}."


class Baterista(Musico):
    """Subclase Baterista que hereda de Musico."""

    def __init__(self, nombre, marca_bateria="Pearl"):
        super().__init__(nombre)
        self.marca_bateria = marca_bateria

    def instrumento(self):
        """Sobrescritura del método instrumento()."""
        return f" {self.nombre} marca el ritmo en la batería {self.marca_bateria}."


def tocar_concierto(lista_musicos):
    """
    Función polimórfica que recibe una lista de Músicos
    y ejecuta instrumento() sin importar la subclase específica.
    """
    print("\n ¡ARRANCA EL CONCIERTO EN VIVO!")
    print("=" * 60)
    for musico in lista_musicos:
        if isinstance(musico, Musico):
            print(f"• {type(musico).__name__:<12}: {musico.instrumento()}")
    print("=" * 60 + "\n")


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 62: POLIMORFISMO EN LA CLASE MUSICO ---")

    # 1. Instanciación de objetos de la jerarquía
    musico_generico = Musico("Carlos")
    guitarrista = Guitarrista("Jimi Hendrix", "Fender Stratocaster")
    baterista = Baterista("Charly Alberti", "Yamaha")

    # 2. Lista heterogénea de músicos (Polimorfismo)
    banda = [musico_generico, guitarrista, baterista]

    # 3. Demostración de respuesta polimórfica
    tocar_concierto(banda)


if __name__ == "__main__":
    main()