class Libro:
    def __init__(self, titulo, autor, isbn):
        
        self.titulo = titulo.strip()
        self.autor = autor.strip() if isinstance(autor, str) else autor
        self.isbn = isbn.strip()

    def mostrar_informacion(self):
        
        autor_nombre = self.autor.nombre if hasattr(self.autor, "nombre") else self.autor
        print(f"📖 Título: {self.titulo}")
        print(f"✍️  Autor:  {autor_nombre}")
        print(f"🔢 ISBN:   {self.isbn}")


class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato, tamano_archivo):
        
        super().__init__(titulo, autor, isbn)
        self.formato = formato.strip()
        self.tamano_archivo = tamano_archivo.strip()

    def mostrar_informacion(self):
        
        super().mostrar_informacion()
        print(f"💾 Formato: {self.formato}")
        print(f"📦 Tamaño:  {self.tamano_archivo}")


class EBook(LibroDigital):
    def __init__(self, titulo, autor, isbn, formato, tamano_archivo, enlace_descarga):
        
        super().__init__(titulo, autor, isbn, formato, tamano_archivo)
        self.enlace_descarga = enlace_descarga.strip()

    def mostrar_informacion(self):
       
        super().mostrar_informacion()
        print(f"🔗 Enlace de Descarga: {self.enlace_descarga}")


if __name__ == "__main__":
    print("\n" + "=" * 65)
    print("=" * 65)
    print()

    # 1. Crear un objeto LibroDigital
    libro_digital = LibroDigital(
        titulo="Cien Años de Soledad",
        autor="Gabriel García Márquez",
        isbn="978-0307474728",
        formato="PDF",
        tamano_archivo="4.5 MB"
    )
    print()
    print("[ Ficha de LibroDigital ]")
    libro_digital.mostrar_informacion()

    print()
    print("-" * 65)
    print()

    # 2. Crear un objeto EBook
    ebook = EBook(
        titulo="El Principito",
        autor="Antoine de Saint-Exupéry",
        isbn="978-0156013987",
        formato="EPUB",
        tamano_archivo="2.1 MB",
        enlace_descarga="www.biblioteca.digital/descargas/el-principito.epub"
    )
    print()
    print("[ Ficha de EBook ]")
    ebook.mostrar_informacion()

    print()
    print("=" * 65)
    print()