class Autor:
    def __init__(self, nombre, nacionalidad="Desconocida"):
        """
        Inicializador de la clase Autor.
        """
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        # Atributo ampliado: lista vacía para almacenar los libros del autor
        self.libros = []

    def agregar_libro(self, titulo_libro):
        """
        Agrega un nuevo libro a la lista del autor, realizando validaciones básicas.
        """
        titulo_limpio = titulo_libro.strip()
        if not titulo_limpio:
            print("[Error]: El título del libro no puede estar vacío.")
            return False
        
        # Evitamos agregar duplicados (insensible a mayúsculas/minúsculas)
        for libro in self.libros:
            if libro.lower() == titulo_limpio.lower():
                print(f"[Error]: El libro '{titulo_limpio}' ya está registrado para el autor {self.nombre}.")
                return False
                
        self.libros.append(titulo_limpio)
        print(f"✔️ Libro '{titulo_limpio}' agregado con éxito a la lista de {self.nombre}.")
        return True

    def eliminar_libro(self, titulo_libro):
        """
        Elimina un libro de la lista del autor si existe.
        """
        titulo_limpio = titulo_libro.strip()
        for i, libro in enumerate(self.libros):
            if libro.lower() == titulo_limpio.lower():
                self.libros.pop(i)
                print(f"❌ Libro '{libro}' eliminado con éxito de la lista de {self.nombre}.")
                return True
                
        print(f"⚠️ El libro '{titulo_limpio}' no se encuentra en la lista de {self.nombre}.")
        return False

    def mostrar_informacion(self):
        """
        Muestra la información del autor y su catálogo de libros.
        """
        print("\n" + "=" * 60)
        print(f"AUTOR: {self.nombre.upper()}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("-" * 60)
        if not self.libros:
            print("📭 No hay libros registrados en su catálogo actualmente.")
        else:
            print("📚 Catálogo de libros escritos:")
            for indice, libro in enumerate(self.libros, 1):
                print(f"   {indice}. {libro}")
        print("=" * 60)


# =====================================================================
# PRUEBAS AUTOMÁTICAS DEL DESAFÍO 47
# =====================================================================
if __name__ == "__main__":
    print("\n>>> INICIANDO PRUEBAS REQUERIDAS DEL DESAFÍO 47 <<<\n")

    # 1. Creamos instancias de Autores utilizando tu catálogo personalizado
    print("--- 1. Creando autores ---")
    autor1 = Autor("Marian Rojas", "Española")
    autor2 = Autor("Lorena Pronsky", "Argentina")
    
    # 2. Agregamos libros a cada autor usando el método de clase 'agregar_libro'
    print("\n--- 2. Agregando libros a las listas de cada autor ---")
    autor1.agregar_libro("Cómo hacer que te pasen cosas buenas")
    autor1.agregar_libro("Encuentra tu persona vitamina")
    
    autor2.agregar_libro("Cúrame")
    autor2.agregar_libro("Despierta") # Otro libro conocido de Lorena Pronsky para la prueba

    # 3. Mostramos la información inicial de los autores
    print("\n--- 3. Mostrando información de catálogos iniciales ---")
    autor1.mostrar_informacion()
    autor2.mostrar_informacion()

    # 4. Probamos eliminar un libro de la lista utilizando 'eliminar_libro'
    print("\n--- 4. Eliminando un libro de la lista ---")
    autor2.eliminar_libro("Despierta")

    # 5. Volvemos a mostrar la información para verificar la actualización de la lista
    print("\n--- 5. Mostrando catálogo actualizado para verificar eliminación ---")
    autor2.mostrar_informacion()

    print("\n>>> PRUEBAS AUTOMÁTICAS FINALIZADAS CON ÉXITO <<<\n")