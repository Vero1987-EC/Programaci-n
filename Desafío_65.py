import math


class Figura:
    """Clase base genérica que representa a una Figura geométrica."""

    def __init__(self, nombre="Figura Genérica"):
        self.__nombre = None
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre de la figura no puede estar vacío.")
        self.__nombre = valor.strip()

    def area(self):
        """
        Método base que debe ser sobrescrito por las subclases.
        """
        raise NotImplementedError("Las subclases deben implementar el método area().")

    def __str__(self):
        return f"{self.nombre} (Área: {self.area():.2f})"


class Circulo(Figura):
    """Subclase Circulo que hereda de Figura."""

    def __init__(self, radio, nombre="Círculo"):
        super().__init__(nombre)
        self.__radio = None
        self.radio = radio

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El radio debe ser un número mayor a cero.")
        self.__radio = float(valor)

    def area(self):
        """Sobrescritura del método area() para el cálculo del Círculo (π * r²)."""
        return math.pi * (self.radio ** 2)


class Cuadrado(Figura):
    """Subclase Cuadrado que hereda de Figura."""

    def __init__(self, lado, nombre="Cuadrado"):
        super().__init__(nombre)
        self.__lado = None
        self.lado = lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El lado debe ser un número mayor a cero.")
        self.__lado = float(valor)

    def area(self):
        """Sobrescritura del método area() para el cálculo del Cuadrado (l²)."""
        return self.lado ** 2


def procesar_figuras_polimorficas(lista_figuras):
    """
    Función polimórfica que recorre cualquier colección de Figuras
    y calcula su área llamando dinámicamente al método sobrescrito.
    """
    print("\n CÁLCULO POLIMÓRFICO DE ÁREAS GEOMÉTRICAS")
    print("=" * 65)
    for idx, figura in enumerate(lista_figuras, 1):
        if isinstance(figura, Figura):
            print(
                f"   {idx}. [{type(figura).__name__:<8}] {figura.nombre:<12} | Área"
                f" calculada: {figura.area():8.2f} u²"
            )
    print("=" * 65 + "\n")


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 65: POLIMORFISMO EN FIGURAS GEOMÉTRICAS ---")
    print("-" * 65)

    # 1. Instanciación de figuras
    c1 = Circulo(radio=5.0, nombre="Círculo R5")
    c2 = Circulo(radio=2.5, nombre="Círculo R2.5")
    q1 = Cuadrado(lado=4.0, nombre="Cuadrado L4")
    q2 = Cuadrado(lado=10.0, nombre="Cuadrado L10")

    # 2. Colección heterogénea de figuras
    figuras = [c1, q1, c2, q2]

    # 3. Procesamiento polimórfico
    procesar_figuras_polimorficas(figuras)


if __name__ == "__main__":
    main()
    