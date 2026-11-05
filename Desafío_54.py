class Autor:
    """Clase Autor encapsulada con decoradores @property."""

    def __init__(self, nombre, nacionalidad):
        # Atributos privados
        self.__nombre = None
        self.__nacionalidad = None

        # Asignación inicial a través de las propiedades validadoras
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    # --- PROPIEDAD NOMBRE ---
    @property
    def nombre(self):
        """Getter para el atributo privado __nombre."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        """Setter con validación para __nombre."""
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(
                "Error de validación: El nombre debe ser una cadena de texto"
                " no vacía."
            )
        self.__nombre = valor.strip()

    # --- PROPIEDAD NACIONALIDAD ---
    @property
    def nacionalidad(self):
        """Getter para el atributo privado __nacionalidad."""
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, valor):
        """Setter con validación para __nacionalidad."""
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(
                "Error de validación: La nacionalidad debe ser una cadena de"
                " texto no vacía."
            )
        self.__nacionalidad = valor.strip()

    def mostrar_autor(self):
        """Muestra los detalles del autor accediendo a las propiedades protegidas."""
        print(f"Nombre:       {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 54: DECORADORES @PROPERTY ---")
    print("-" * 60)

    # 1. Instanciación limpia usando la interfaz de propiedades
    autor = Autor("Marian Rojas Estapé", "Española")
    autor.mostrar_autor()
    print("-" * 60)

    # 2. Lectura y modificación elegante estilo atributo
    print("Modificación sintáctica de atributos vía Setter:")
    autor.nombre = "Marian Rojas"
    autor.nacionalidad = "Española / Internacional"
    print(f"Lectura directa -> autor.nombre:       '{autor.nombre}'")
    print(f"Lectura directa -> autor.nacionalidad: '{autor.nacionalidad}'")
    print("-" * 60)

    # 3. Prueba de bloqueo con datos no válidos
    print("Intento de asignación de un valor inválido (cadena vacía):")
    try:
        autor.nombre = "   "
    except ValueError as e:
        print(f" Capturado por el @setter: {e}")

    print("-" * 60)


if __name__ == "__main__":
    main()