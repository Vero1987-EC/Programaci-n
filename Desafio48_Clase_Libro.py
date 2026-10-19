
class Autor:
    def __init__(self, nombre, nacionalidad="Desconocida"):
        """
        Inicializador de la clase Autor.
        """
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        # En el Desafío 47 guardábamos strings. 
        # Ahora esta lista almacenará objetos reales de la clase Libro (Asociación).
        self.libros = []

    def agregar_libro(self, libro_objeto):
        """
        Recibe un objeto de la clase Libro y lo agrega al catálogo del autor.
        """
        # Validación: nos aseguramos de que realmente sea un objeto Libro
        if not isinstance(libro_objeto, Libro):
            print(f"[Error]: '{libro_objeto}' no es un objeto de la clase Libro.")
            return False
        
        # Evitamos duplicados comparando por su identificador único (ISBN)
        for l in self.libros:
            if l.isbn == libro_objeto.isbn:
                print(f"[Error]: El libro con ISBN {libro_objeto.isbn} ya está registrado para {self.nombre}.")
                return False
                
        self.libros.append(libro_objeto)
        return True

    def mostrar_informacion(self):
        """
        Muestra la información del autor y el catálogo de sus objetos Libro.
        """
        print("\n" + "=" * 70)
        print(f"AUTOR: {self.nombre.upper()} | Nacionalidad: {self.nacionalidad}")
        print("-" * 70)
        if not self.libros:
            print("📭 No hay libros registrados en su catálogo actualmente.")
        else:
            print("📚 Catálogo de libros escritos (Objetos relacionados):")
            for indice, libro in enumerate(self.libros, 1):
                print(f"   {indice}. '{libro.titulo}' | Género: {libro.genero} | ISBN: {libro.isbn}")
        print("=" * 70)


class Libro:
    def __init__(self, titulo, genero, isbn, autor_instancia=None):
        """
        Inicializador de la clase Libro con atributos básicos y relación con Autor.
        """
        self.titulo = titulo.strip()
        self.genero = genero.strip()
        self.isbn = isbn.strip()
        
        # RELACIÓN: Asociamos este libro con una instancia de la clase Autor
        self.autor = autor_instancia
        
        # Si al crear el libro le pasamos un objeto Autor válido, 
        # vinculamos el libro automáticamente a la lista del autor.
        if autor_instancia is not None and isinstance(autor_instancia, Autor):
            autor_instancia.agregar_libro(self)

    def mostrar_detalle(self):
        """
        Muestra la ficha técnica del libro y los datos de su autor relacionado.
        """
        print("\n" + "-" * 50)
        print(f"📖 FICHA TÉCNICA DEL LIBRO")
        print("-" * 50)
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"ISBN:   {self.isbn}")
        if self.autor:
            print(f"Autor:  {self.autor.nombre} ({self.autor.nacionalidad})")
        else:
            print("Autor:  No especificado / Anónimo")
        print("-" * 50)


# =====================================================================
# DEMOSTRACIÓN DE LA RELACIÓN ENTRE CLASES
# =====================================================================
if __name__ == "__main__":
    print("\n>>> INICIANDO PRUEBAS REQUERIDAS DEL DESAFÍO 48 <<<\n")

    # 1. Creamos las instancias de Autor (al igual que en tus desafíos anteriores)
    print("--- 1. Creamos objetos Autor ---")
    autor1 = Autor("Marian Rojas", "Española")
    autor2 = Autor("Lorena Pronsky", "Argentina")
    print(f"✔️ Objeto Autor creado: {autor1.nombre}")
    print(f"✔️ Objeto Autor creado: {autor2.nombre}")

    # 2. Creamos los objetos Libro relacionándolos directamente con sus Autores
    print("\n--- 2. Creando objetos Libro asociados a sus autores ---")
    
    # Creamos libros de Marian Rojas y pasamos el objeto 'autor1' como argumento
    libro1 = Libro("Cómo hacer que te pasen cosas buenas", "Desarrollo Personal", "978-84-670-5339-5", autor1)
    libro2 = Libro("Encuentra tu persona vitamina", "Psicología", "978-84-670-6290-8", autor1)

    # Creamos un libro de Lorena Pronsky y pasamos el objeto 'autor2' como argumento
    libro3 = Libro("Cúrame", "Desarrollo Emocional", "978-950-49-7312-6", autor2)

    # 3. Mostramos las fichas de los libros individuales
    # Verás que cada libro sabe quién es su autor accediendo a 'self.autor.nombre'
    print("\n--- 3. Mostrando fichas técnicas individuales ---")
    libro1.mostrar_detalle()
    libro3.mostrar_detalle()

    # 4. Mostramos la información de los autores
    # Verás que los autores tienen la colección de objetos Libro en su atributo 'libros'
    print("\n--- 4. Mostrando información de autores y sus catálogos ---")
    autor1.mostrar_informacion()
    autor2.mostrar_informacion()

    print("\n>>> PRUEBAS AUTOMÁTICAS FINALIZADAS CON ÉXITO <<<\n")