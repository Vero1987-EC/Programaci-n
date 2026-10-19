"""
Desafío 57: Herencia — Clase Poeta
Asignatura: PROGRAMACIÓN I

Este programa implementa la clase Poeta como una subclase (hija) de Autor (padre),
demostrando la reutilización de código mediante Herencia, el uso de super()
y la adición de atributos y métodos específicos para Poeta.
"""

class Autor:
    def __init__(self, nombre, nacionalidad="Desconocida"):
        """
        Constructor de la clase base Autor.
        Inicializa los atributos básicos y la lista de libros/obras.
        """
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

    def agregar_libro(self, titulo_libro):
        """
        Método heredable para agregar una obra al catálogo del autor.
        """
        titulo_limpio = titulo_libro.strip()
        if not titulo_limpio:
            print("❌ [Error]: El título no puede estar vacío.")
            return False
            
        for libro in self.libros:
            if libro.lower() == titulo_limpio.lower():
                print(f"⚠️ El título '{titulo_limpio}' ya está registrado en el catálogo de {self.nombre}.")
                return False
                
        self.libros.append(titulo_limpio)
        print(f"✔️ Obra '{titulo_limpio}' agregada con éxito al catálogo de {self.nombre}.")
        return True

    def mostrar_informacion(self):
        """
        Muestra la información general del autor.
        """
        print("\n" + "=" * 60)
        print(f"👤 AUTOR: {self.nombre.upper()}")
        print(f"🌐 Nacionalidad: {self.nacionalidad}")
        if self.libros:
            print(f"📚 Obras registradas ({len(self.libros)}):")
            for idx, obra in enumerate(self.libros, 1):
                print(f"   {idx}. {obra}")
        else:
            print("📭 No hay obras registradas en su catálogo actualmente.")
        print("=" * 60)


class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        """
        Constructor de la subclase Poeta.
        Utiliza super() para inicializar los atributos heredados de Autor
        y agrega el atributo específico tipo_poesia.
        """
        # Inicialización de atributos heredados usando super()
        super().__init__(nombre, nacionalidad)
        # Atributo nuevo y exclusivo de Poeta
        self.tipo_poesia = tipo_poesia

    def mostrar_informacion_poeta(self):
        """
        Método específico de Poeta que muestra toda la información:
        nombre, nacionalidad y tipo de poesía (además de sus poemarios si existen).
        """
        print("\n" + "=" * 60)
        print(f"✒️ POETA: {self.nombre.upper()}")
        print(f"🌐 Nacionalidad: {self.nacionalidad}")
        print(f"📜 Tipo de Poesía: {self.tipo_poesia}")
        if self.libros:
            print(f"📚 Poemarios/Obras registradas ({len(self.libros)}):")
            for idx, obra in enumerate(self.libros, 1):
                print(f"   {idx}. {obra}")
        else:
            print("📭 No hay poemarios registrados actualmente.")
        print("=" * 60)


# =============================================================================
# BLOQUE PRINCIPAL DE DEMOSTRACIÓN Y PRUEBAS
# =============================================================================
if __name__ == "__main__":
    print("\n>>> INICIANDO PRUEBAS DEL DESAFÍO 57 (HERENCIA - CLASE POETA) <<<\n")

    # 1. Creación de al menos dos objetos Poeta
    print("--- 1. Creando objetos de la clase Poeta ---")
    poeta1 = Poeta("Pablo Neruda", "Chilena", "Poesía Amorosa y Neorromántica")
    poeta2 = Poeta("Mario Benedetti", "Uruguaya", "Poesía Coloquial y Social")
    print(f"✔️ Objeto Poeta 1 creado: {poeta1.nombre}")
    print(f"✔️ Objeto Poeta 2 creado: {poeta2.nombre}")

    # 2. Mostrar sus datos completos usando el método de Poeta
    print("\n--- 2. Mostrando datos de los poetas ---")
    poeta1.mostrar_informacion_poeta()
    poeta2.mostrar_informacion_poeta()

    # 3. Verificación de uso de atributos y métodos HEREDADOS de Autor
    print("\n--- 3. Verificando métodos y atributos HEREDADOS de la clase Autor ---")
    print("A) Invocando el método heredado 'agregar_libro'...")
    poeta1.agregar_libro("Veinte poemas de amor y una canción desesperada")
    poeta1.agregar_libro("Canto General")
    
    poeta2.agregar_libro("El cumpleaños de Juan Ángel")
    poeta2.agregar_libro("Inventario uno")

    print("\nB) Invocando el método heredado 'mostrar_informacion()' del padre (Autor)...")
    poeta1.mostrar_informacion()

    print("\nC) Mostrando ficha técnica completa actualizada del Poeta...")
    poeta2.mostrar_informacion_poeta()

    print("\n>>> PRUEBAS AUTOMÁTICAS FINALIZADAS CON ÉXITO <<<\n")