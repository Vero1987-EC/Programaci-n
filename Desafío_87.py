import os

def buscar_libros_por_autor(nombre_archivo, autor_buscado):
    # Auto-crear libros.txt con datos iniciales si no existe en la carpeta
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("Cien años de soledad - Gabriel García Márquez\n")
            f.write("1984 - George Orwell\n")
            f.write("Fahrenheit 451 - Ray Bradbury\n")

    coincidencias = []
    autor_clean = autor_buscado.strip().lower()

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if autor_clean in linea.lower():
                    coincidencias.append(linea.strip())

        if coincidencias:
            print(f"\n Libros encontrados de '{autor_buscado}':")
            for libro in coincidencias:
                print(f"  • {libro}")
        else:
            print(f"\n No se encontraron coincidencias para '{autor_buscado}'.")
    except FileNotFoundError:
        print(f" Error: El archivo '{nombre_archivo}' no existe.")

if __name__ == "__main__":
    autor = input("Ingrese el nombre del autor a buscar: ")
    buscar_libros_por_autor("libros.txt", autor)