
import math


class Figura:
    """Clase base que define la interfaz común para las figuras geométricas."""

    def area(self):
        """Calcula el área de la figura. Debe ser sobrescrito por las subclases."""
        pass


class Circulo(Figura):
    """Subclase que representa un círculo."""

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        """Calcula el área de un círculo (pi * radio^2)."""
        return math.pi * (self.radio**2)


class Cuadrado(Figura):
    """Subclase que representa un cuadrado."""

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        """Calcula el área de un cuadrado (lado^2)."""
        return self.lado**2


def main():
    # Instanciación de objetos de distintas subclases
    figuras = [
        Circulo(radio=5),
        Cuadrado(lado=4),
        Circulo(radio=3),
        Cuadrado(lado=6),
    ]

    print("Cálculo de Áreas - Demostración de Polimorfismo")
    print("-" * 45)

    # Recorrido polimórfico
    for figura in figuras:
        nombre = figura.__class__.__name__
        resultado_area = figura.area()
        print(f"Figura: {nombre:<10} | Área: {resultado_area:.2f}")

    print("-" * 45)


if __name__ == "__main__":
    main()