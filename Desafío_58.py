class Usuario:
    """Clase base encapsulada que representa a un Usuario del sistema."""

    def __init__(self, nombre, id_usuario, email):
        self.__nombre = None
        self.__id_usuario = None
        self.__email = None

        self.nombre = nombre
        self.id_usuario = id_usuario
        self.email = email

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        if not isinstance(valor, (str, int)) or not str(valor).strip():
            raise ValueError("El ID de usuario no puede estar vacío.")
        self.__id_usuario = str(valor).strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or "@" not in valor:
            raise ValueError("El email debe ser una dirección válida.")
        self.__email = valor.strip()

    def mostrar_informacion(self):
        print(f"Usuario: {self.nombre} [ID: {self.id_usuario}] | Email: {self.email}")


class Bibliotecario(Usuario):
    """
    Subclase Bibliotecario que hereda de Usuario.
    Añade atributos específicos: 'seccion' y 'anos_experiencia'.
    """

    def __init__(self, nombre, id_usuario, email, seccion, anos_experiencia):
        # Invocación del constructor de la superclase
        super().__init__(nombre, id_usuario, email)
        self.__seccion = None
        self.__anos_experiencia = None

        self.seccion = seccion
        self.anos_experiencia = anos_experiencia

    @property
    def seccion(self):
        return self.__seccion

    @seccion.setter
    def seccion(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La sección debe ser una cadena no vacía.")
        self.__seccion = valor.strip()

    @property
    def anos_experiencia(self):
        return self.__anos_experiencia

    @anos_experiencia.setter
    def anos_experiencia(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("Los años de experiencia deben ser un entero no negativo.")
        self.__anos_experiencia = valor

    def gestionar_prestamo(self, libro_titulo, usuario_nombre):
        """Método especializado del bibliotecario."""
        print(
            f" El bibliotecario {self.nombre} (Sección {self.seccion}) registró el préstamo del libro '{libro_titulo}' a {usuario_nombre}."
        )

    def mostrar_informacion(self):
        """Sobrescribe mostrar_informacion para incluir datos del cargo."""
        super().mostrar_informacion()
        print(
            f"Cargo: Bibliotecario | Sección: {self.seccion} | Experiencia: {self.anos_experiencia} año(s)"
        )


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 58: CLASE BIBLIOTECARIO (HERENCIA) ---")
    print("-" * 65)

    # 1. Instanciación de un Bibliotecario
    b1 = Bibliotecario(
        nombre="Valeria Gómez",
        id_usuario="BIB-2026-04",
        email="valeria.gomez@biblioteca.edu.ar",
        seccion="Ficción y Literatura Contemporánea",
        anos_experiencia=8,
    )

    # 2. Mostrar información general y específica
    print("Ficha del Bibliotecario:")
    b1.mostrar_informacion()

    print("-" * 65)
    # 3. Invocación de un método especializado de gestión
    b1.gestionar_prestamo("Cien años de soledad", "Carlos Pérez")

    print("-" * 65)


if __name__ == "__main__":
    main()