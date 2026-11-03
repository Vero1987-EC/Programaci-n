class Personaje:
    """Clase base que representa la interfaz común de cualquier personaje."""

    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def atacar(self):
        """Método base diseñado para ser sobrescrito por las subclases."""
        pass


class Guerrero(Personaje):
    """Subclase específica para el tipo Guerrero."""

    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida)
        self.fuerza = fuerza

    def atacar(self):
        daño = self.fuerza * 2
        print(f"{self.nombre} (Guerrero) ataca con espada causando {daño} de daño físico.")


class Mago(Personaje):
    """Subclase específica para el tipo Mago."""

    def __init__(self, nombre, vida, mana):
        super().__init__(nombre, vida)
        self.mana = mana

    def atacar(self):
        daño = int(self.mana * 1.5)
        print(f"{self.nombre} (Mago) lanza un hechizo causando {daño} de daño mágico.")


class Arquero(Personaje):
    """Nueva subclase agregada sin necesidad de modificar el código existente."""

    def __init__(self, nombre, vida, agilidad):
        super().__init__(nombre, vida)
        self.agilidad = agilidad

    def atacar(self):
        daño = self.agilidad * 3
        print(f"{self.nombre} (Arquero) dispara una flecha causando {daño} de daño a distancia.")


def main():
    print("Simulación de Videojuego - Demostración de Extensibilidad")
    print("-" * 60)

    # Colección polimórfica de personajes
    equipo = [
        Guerrero("Thorin", 100, fuerza=25),
        Mago("Gandalf", 80, mana=40),
        Arquero("Legolas", 90, agilidad=20)
    ]

    # Recorrido polimórfico: ejecución del método atacar() sin condicionales
    for personaje in equipo:
        personaje.atacar()

    print("-" * 60)


if __name__ == "__main__":
    main()