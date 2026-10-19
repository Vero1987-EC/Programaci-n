
# Estructura de almacenamiento del TAD: Lista de libros
# Cada libro será representado como un diccionario con: título, autor y año de publicación.
biblioteca = []

# =====================================================================
# FUNCIONES DEL TAD BIBLIOTECA
# =====================================================================

def agregar_libro(titulo, autor, año):
    """
    Agrega un nuevo libro a la biblioteca realizando validaciones básicas.
    """
    # Validamos que los campos de texto no estén vacíos
    if not titulo.strip() or not autor.strip():
        print("[Error]: El título y el autor no pueden estar vacíos.")
        return False
    
    # Validamos el año (debe ser un número entero razonable)
    try:
        año_int = int(año)
        if año_int < 0 or año_int > 2026:
            print("[Error]: Por favor, ingrese un año de publicación válido.")
            return False
    except ValueError:
        print("[Error]: El año de publicación debe ser un número entero.")
        return False

    # Evitamos duplicados exactos por título (insensible a mayúsculas/minúsculas)
    for libro in biblioteca:
        if libro["titulo"].lower().strip() == titulo.lower().strip():
            print(f"[Error]: El libro '{titulo}' ya existe en la biblioteca.")
            return False

    # Creamos el diccionario que representa el libro (TAD)
    nuevo_libro = {
        "titulo": titulo.strip(),
        "autor": autor.strip(),
        "año": año_int
    }
    
    # Agregamos el libro a la lista
    biblioteca.append(nuevo_libro)
    print(f"✔️ ¡Libro '{titulo}' agregado con éxito!")
    return True


def eliminar_libro(titulo):
    """
    Elimina un libro de la biblioteca buscando por su título exacto
    (insensible a mayúsculas y minúsculas).
    """
    if not titulo.strip():
        print("[Error]: Debe ingresar un título válido para eliminar.")
        return False

    for i, libro in enumerate(biblioteca):
        if libro["titulo"].lower().strip() == titulo.lower().strip():
            libro_eliminado = biblioteca.pop(i)
            print(f"❌ ¡Libro '{libro_eliminado['titulo']}' eliminado de la biblioteca con éxito!")
            return True
            
    # Caso donde el libro no se encuentra
    print(f"⚠️ No se encontró ningún libro con el título '{titulo}' para eliminar.")
    return False


def buscar_libro(titulo):
    """
    Busca libros en la colección que contengan el título ingresado
    (insensible a mayúsculas/minúsculas y permite coincidencias parciales).
    """
    if not titulo.strip():
        print("[Error]: Debe ingresar un título para realizar la búsqueda.")
        return []

    coincidencias = []
    for libro in biblioteca:
        # Búsqueda parcial e insensible a mayúsculas/minúsculas
        if titulo.lower().strip() in libro["titulo"].lower():
            coincidencias.append(libro)
            
    return coincidencias


def mostrar_biblioteca():
    """
    Muestra de forma clara, ordenada y amigable todos los libros disponibles.
    Adaptado con anchos de columna dinámicos para títulos y autores más largos.
    """
    if len(biblioteca) == 0:
        print("\n📭 La biblioteca está vacía. No hay libros registrados.")
        return

    print("\n" + "=" * 80)
    print(f"{'LIBROS DISPONIBLES EN LA BIBLIOTECA':^80}")
    print("=" * 80)
    # Encabezado con formato de columnas tabuladas
    print(f"{'N°':<4} | {'TÍTULO':<38} | {'AUTOR':<22} | {'AÑO':<6}")
    print("-" * 80)
    
    for indice, libro in enumerate(biblioteca, 1):
        # Limitamos los caracteres a mostrar para evitar roturas visuales si el texto es excesivamente largo
        tit_formateado = libro['titulo'][:36] + '..' if len(libro['titulo']) > 38 else libro['titulo']
        aut_formateado = libro['autor'][:20] + '..' if len(libro['autor']) > 22 else libro['autor']
        print(f"{indice:<4} | {tit_formateado:<38} | {aut_formateado:<22} | {libro['año']:<6}")
    print("=" * 80 + "\n")


# =====================================================================
# PRUEBAS DEL TAD (Requerido por la consigna del desafío)
# =====================================================================
def ejecutar_pruebas_automaticas():
    print("\n>>> INICIANDO PRUEBAS REQUERIDAS DEL DESAFÍO <<<\n")
    
    # 1. Agregar al menos 4 libros personalizados solicitados por el usuario
    print("--- 1. Agregando 4 libros de prueba personalizados ---")
    agregar_libro("COMO HACER QUE TE PASEN COSAS BUENAS", "Marian Rojas", "2018")
    agregar_libro("COMO DEJAR DE PENSAR DEMASIADO", "Adam Tusco", "2020")
    agregar_libro("ESTE DOLOR NO ES MIO", "Mark Wolynn", "2016")
    agregar_libro("CURAME", "Lorena Pronsky", "2022")
    
    # 2. Mostrar la biblioteca con los libros agregados
    mostrar_biblioteca()
    
    # 3. Realizar una búsqueda (por ejemplo, buscar "dolor")
    termino_busqueda = "dolor"
    print(f"--- 2. Buscando libro por título: '{termino_busqueda}' ---")
    resultados = buscar_libro(termino_busqueda)
    if resultados:
        print(f"🔍 Se encontraron {len(resultados)} coincidencia(s):")
        for r in resultados:
            print(f"   -> Título: {r['titulo']} | Autor: {r['autor']} | Año: {r['año']}")
    else:
        print("🔍 No se encontraron coincidencias.")
    print("-" * 80 + "\n")

    # 4. Eliminar uno de ellos (por ejemplo, eliminamos "CURAME")
    libro_a_eliminar = "CURAME"
    print(f"--- 3. Eliminando el libro: '{libro_a_eliminar}' ---")
    eliminar_libro(libro_a_eliminar)
    
    # 5. Mostrar la biblioteca final para verificar la eliminación
    print("\n--- 4. Biblioteca final actualizada ---")
    mostrar_biblioteca()
    
    print(">>> PRUEBAS AUTOMÁTICAS FINALIZADAS CON ÉXITO <<<\n")


# =====================================================================
# INTERFAZ DEDICADA: MENÚ INTERACTIVO (Opcional, ideal para pruebas del alumno)
# =====================================================================
def menu_interactivo():
    while True:
        print("\n" + "*" * 40)
        print("          MENÚ DE LA BIBLIOTECA         ")
        print("*" * 40)
        print("1. Agregar un nuevo libro")
        print("2. Eliminar un libro")
        print("3. Buscar un libro por título")
        print("4. Mostrar todos los libros disponibles")
        print("5. Salir del programa")
        print("*" * 40)
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            print("\n--- AGREGAR LIBRO ---")
            t = input("Título: ")
            a = input("Autor: ")
            y = input("Año de publicación: ")
            agregar_libro(t, a, y)
            
        elif opcion == "2":
            print("\n--- ELIMINAR LIBRO ---")
            t = input("Ingrese el título del libro que desea eliminar: ")
            eliminar_libro(t)
            
        elif opcion == "3":
            print("\n--- BUSCAR LIBRO ---")
            t = input("Ingrese el título (o parte de él) para buscar: ")
            resultados = buscar_libro(t)
            if resultados:
                print(f"\n🔍 Se encontraron {len(resultados)} coincidencia(s):")
                for r in resultados:
                    print(f"   • Título: {r['titulo']} | Autor: {r['autor']} | Año: {r['año']}")
            else:
                print("\n🔍 No se encontraron libros con ese término.")
                
        elif opcion == "4":
            mostrar_biblioteca()
            
        elif opcion == "5":
            print("\n¡Gracias por utilizar el sistema de gestión de biblioteca! Hasta luego.")
            break
        else:
            print("\n❌ Opción no válida. Por favor, seleccione un número del 1 al 5.")


if __name__ == "__main__":
    # Primero ejecutamos las pruebas obligatorias de la consigna del Desafío 44
    ejecutar_pruebas_automaticas()
    
    # Preguntamos al usuario si desea utilizar el menú interactivo para sus propias pruebas
    activar_menu = input("¿Desea ingresar al menú interactivo para realizar más pruebas? (s/n): ").strip().lower()
    if activar_menu == "s":
        menu_interactivo()