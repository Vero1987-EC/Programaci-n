class Autor:
    def __init__(self, nombre, nacionalidad):
        """
        Constructor de la clase Autor.
        Inicializa los atributos privados a través de las propiedades (setters)
        para asegurar que se apliquen las validaciones desde el momento de la creación.
        """
        # Atributos privados inicializados a None antes de invocar los setters
        self._nombre = None
        self._nacionalidad = None
        
        # Asignación a través de las propiedades para reutilizar la lógica de validación
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    # =========================================================================
    # PROPIEDAD: NOMBRE
    # =========================================================================
    @property
    def nombre(self):
        """Getter para el atributo privado _nombre."""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """
        Setter para el atributo privado _nombre.
        Valida que el valor ingresado no sea una cadena vacía ni contenga solo espacios.
        """
        if not isinstance(nuevo_nombre, str) or not nuevo_nombre.strip():
            print("❌ [Error]: El nombre no puede estar vacío ni contener solo espacios.")
            return False
        
        self._nombre = nuevo_nombre.strip()
        print(f"✔️ Nombre actualizado exitosamente a: '{self._nombre}'")
        return True

    # =========================================================================
    # PROPIEDAD: NACIONALIDAD
    # =========================================================================
    @property
    def nacionalidad(self):
        """Getter para el atributo privado _nacionalidad."""
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        """
        Setter para el atributo privado _nacionalidad.
        Valida que el valor ingresado no sea una cadena vacía ni contenga solo espacios.
        """
        if not isinstance(nueva_nacionalidad, str) or not nueva_nacionalidad.strip():
            print("❌ [Error]: La nacionalidad no puede estar vacía ni contener solo espacios.")
            return False
        
        self._nacionalidad = nueva_nacionalidad.strip()
        print(f"✔️ Nacionalidad actualizada exitosamente a: '{self._nacionalidad}'")
        return True

    def mostrar_info(self):
        """Muestra los datos del autor accediendo a las propiedades."""
        print("-" * 50)
        print(f"👤 DATOS DEL AUTOR")
        print(f"   • Nombre:       {self.nombre}")
        print(f"   • Nacionalidad: {self.nacionalidad}")
        print("-" * 50)


# =============================================================================
# BLOQUE PRINCIPAL DE DEMOSTRACIÓN Y PRUEBAS
# =============================================================================
if __name__ == "__main__":
    print("\n>>> INICIANDO PRUEBAS DEL DESAFÍO 54 (ENCAPSULAMIENTO CON @PROPERTY) <<<\n")

    # 1. Crear un objeto Autor
    print("--- 1. Creación inicial del objeto Autor ---")
    autor1 = Autor("Marian Rojas Estapé", "Española")
    
    # 2. Mostrar sus datos utilizando las propiedades (getters)
    print("\n--- 2. Lectura de datos mediante propiedades (Getters) ---")
    autor1.mostrar_info()

    # 3. Modificar su nombre o nacionalidad mediante los setter
    print("\n--- 3. Modificación válida usando Setters ---")
    print("Modificando nacionalidad a 'Española-Argentina'...")
    autor1.nacionalidad = "Española-Argentina"
    
    print("\nModificando nombre a 'Marian Rojas'...")
    autor1.nombre = "Marian Rojas"

    print("\nVerificando los datos actualizados:")
    autor1.mostrar_info()

    # 4. Intentar asignar valores vacíos y observar la respuesta del programa
    print("\n--- 4. Intento de asignación de valores vacíos (Validación de errores) ---")
    
    print("A) Intentando asignar nombre vacío ('') ...")
    autor1.nombre = ""
    
    print("\nB) Intentando asignar nacionalidad con puros espacios ('   ') ...")
    autor1.nacionalidad = "   "

    print("\nVerificando que los datos del autor se mantuvieron intactos:")
    autor1.mostrar_info()

    print("\n>>> PRUEBAS AUTOMÁTICAS FINALIZADAS CON ÉXITO <<<\n")
