
# =====================================================================
# FUNCIONES GENÉRICAS DEL TAD BIBLIOTECA
# =====================================================================

def agregar_libro(coleccion, titulo, autor, anio):
    """
    Agrega un nuevo libro a la colección específica pasada como argumento.
    """
    if not titulo.strip() or not autor.strip():
        print("[Error]: El título y el autor no pueden estar vacíos.")
        return False
    
    try:
        año_int = int(anio)
        if año_int < 0 or año_int > 2026:
            print("[Error]: Por favor, ingrese un año de publicación válido.")
            return False
    except ValueError:
        print("[Error]: El año de publicación debe ser un número entero.")
        return False

    # Evitamos duplicados en la colección específica
    for libro in coleccion:
        if libro["titulo"].lower().strip() == titulo.lower().strip():
            print(f"[Error]: El libro '{titulo}' ya existe en esta colección.")
            return False

    nuevo_libro = {
        "titulo": titulo.strip(),
        "autor": autor.strip(),
        "año": año_int
    }
    
    coleccion.append(nuevo_libro)
    print(f"✔️ ¡Libro '{titulo}' agregado con éxito!")
    return True


def eliminar_libro(coleccion, titulo):
    """
    Elimina un libro de la colección específica buscando por su título.
    """
    if not titulo.strip():
        print("[Error]: Debe ingresar un título válido para eliminar.")
        return False

    for i, libro in enumerate(coleccion):
        if libro["titulo"].lower().strip() == titulo.lower().strip():
            libro_eliminado = coleccion.pop(i)
            print(f"❌ ¡Libro '{libro_eliminado['titulo']}' eliminado con éxito!")
            return True
            
    print(f"⚠️ No se encontró el libro '{titulo}' en esta colección.")
    return False


def buscar_libro(coleccion, titulo):
    """
    Busca libros en la colección específica que contengan el término ingresado.
    """
    if not titulo.strip():
        print("[Error]: Debe ingresar un término para buscar.")
        return []

    coincidencias = []
    for libro in coleccion:
        if titulo.lower().strip() in libro["titulo"].lower():
            coincidencias.append(libro)
            
    return coincidencias


def mostrar_biblioteca(coleccion, nombre_biblioteca):
    """
    Muestra de forma clara y organizada los libros de una colección específica.
    """
    print("\n" + "=" * 80)
    print(f"{nombre_biblioteca.upper():^80}")
    print("=" * 80)
    
    if len(coleccion) == 0:
        print(f"📭 La '{nombre_biblioteca}' está vacía actualmente.")
        print("=" * 80 + "\n")
        return

    print(f"{'N°':<4} | {'TÍTULO':<38} | {'AUTOR':<22} | {'AÑO':<6}")
    print("-" * 80)
    
    for indice, libro in enumerate(coleccion, 1):
        tit_formateado = libro['titulo'][:36] + '..' if len(libro['titulo']) > 38 else libro['titulo']
        aut_formateado = libro['autor'][:20] + '..' if len(libro['autor']) > 22 else libro['autor']
        print(f"{indice:<4} | {tit_formateado:<38} | {aut_formateado:<22} | {libro['año']:<6}")
    print("=" * 80 + "\n")


# =====================================================================
# PRUEBAS DEL DESAFÍO (Demostración de Independencia)
# =====================================================================
def ejecutar_pruebas_multiples():
    print("\n>>> INICIANDO PRUEBAS REQUERIDAS DEL DESAFÍO 45 <<<\n")
    
    # Declaramos las dos colecciones independientes
    biblioteca_personal = []
    biblioteca_estudio = []
    
    # 1. Agregar libros de forma independiente a cada biblioteca
    print("--- 1. Agregando libros a la BIBLIOTECA PERSONAL ---")
    agregar_libro(biblioteca_personal, "COMO HACER QUE TE PASEN COSAS BUENAS", "Marian Rojas", "2018")
    agregar_libro(biblioteca_personal, "COMO DEJAR DE PENSAR DEMASIADO", "Adam Tusco", "2020")
    
    print("\n--- 2. Agregando libros a la BIBLIOTECA de ESTUDIO ---")
    agregar_libro(biblioteca_estudio, "ESTE DOLOR NO ES MIO", "Mark Wolynn", "2016")
    agregar_libro(biblioteca_estudio, "CURAME", "Lorena Pronsky", "2022")
    
    # Mostrar el contenido inicial de ambas
    print("\n--- 3. Mostrando contenido inicial de ambas colecciones ---")
    mostrar_biblioteca(biblioteca_personal, "Biblioteca de Crecimiento Personal")
    mostrar_biblioteca(biblioteca_estudio, "Biblioteca de Estudio Académico")
    
    # 4. Búsqueda cruzada para verificar que no hay interferencias
    print("--- 4. Realizando búsquedas independientes ---")
    print("Buscando 'PENSAR' en Biblioteca Personal:")
    resultados_pers = buscar_libro(biblioteca_personal, "PENSAR")
    for r in resultados_pers:
        print(f"   -> Encontrado: {r['titulo']} ({r['año']})")
        
    print("\nBuscando 'PENSAR' en Biblioteca de Estudio:")
    resultados_est = buscar_libro(biblioteca_estudio, "PENSAR")
    if not resultados_est:
        print("   🔍 No se encontraron coincidencias (¡Comportamiento correcto e independiente!)")
    print("-" * 80 + "\n")
    
    # 5. Eliminar un libro de una colección sin afectar la otra
    print("--- 5. Eliminando 'CURAME' de Biblioteca de Estudio ---")
    eliminar_libro(biblioteca_estudio, "CURAME")
    
    print("\n--- 6. Verificando que Biblioteca Personal se mantiene intacta ---")
    mostrar_biblioteca(biblioteca_personal, "Biblioteca de Crecimiento Personal")
    mostrar_biblioteca(biblioteca_estudio, "Biblioteca de Estudio Académico")
    
    print(">>> PRUEBAS AUTOMÁTICAS DEL DESAFÍO 45 FINALIZADAS CON ÉXITO <<<\n")
    return biblioteca_personal, biblioteca_estudio


# =====================================================================
# MENÚ INTERACTIVO CON SELECCIÓN DE BIBLIOTECA
# =====================================================================
def menu_interactivo(bib_pers, bib_est):
    # Diccionario para mapear la biblioteca seleccionada
    bibliotecas_disponibles = {
        "1": (bib_pers, "Biblioteca de Crecimiento Personal"),
        "2": (bib_est, "Biblioteca de Estudio Académico")
    }
    
    while True:
        print("\n" + "*" * 40)
        print("     GESTOR DE MÚLTIPLES BIBLIOTECAS    ")
        print("*" * 40)
        print("1. Gestionar Biblioteca Personal")
        print("2. Gestionar Biblioteca de Estudio")
        print("3. Mostrar ambas bibliotecas juntas")
        print("4. Salir")
        print("*" * 40)
        
        opcion_principal = input("Seleccione una opción: ").strip()
        
        if opcion_principal == "4":
            print("\n¡Gracias por utilizar el sistema! Hasta luego.")
            break
            
        elif opcion_principal == "3":
            mostrar_biblioteca(bib_pers, "Biblioteca de Crecimiento Personal")
            mostrar_biblioteca(bib_est, "Biblioteca de Estudio Académico")
            
        elif opcion_principal in ["1", "2"]:
            coleccion_activa, nombre_activo = bibliotecas_disponibles[opcion_principal]
            
            # Submenú para la biblioteca seleccionada
            while True:
                print(f"\n--- GESTIONANDO: {nombre_activo.upper()} ---")
                print("1. Agregar libro")
                print("2. Eliminar libro")
                print("3. Buscar libro")
                print("4. Mostrar libros")
                print("5. Volver al menú principal")
                print("-" * 40)
                
                opcion_sub = input("Opción: ").strip()
                
                if opcion_sub == "1":
                    t = input("Título: ")
                    a = input("Autor: ")
                    y = input("Año de publicación: ")
                    agregar_libro(coleccion_activa, t, a, y)
                elif opcion_sub == "2":
                    t = input("Ingrese el título del libro a eliminar: ")
                    eliminar_libro(coleccion_activa, t)
                elif opcion_sub == "3":
                    t = input("Ingrese término de búsqueda: ")
                    res = buscar_libro(coleccion_activa, t)
                    if res:
                        print(f"\n🔍 {len(res)} coincidencias encontradas:")
                        for r in res:
                            print(f"   • {r['titulo']} | Autor: {r['autor']} | Año: {r['año']}")
                    else:
                        print("\n🔍 Sin coincidencias en esta biblioteca.")
                elif opcion_sub == "4":
                    mostrar_biblioteca(coleccion_activa, nombre_activo)
                elif opcion_sub == "5":
                    break
                else:
                    print("❌ Opción inválida.")
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    # Ejecutamos la simulación e inicializamos las listas con el retorno de las pruebas
    b_personal, b_estudio = ejecutar_pruebas_multiples()
    
    activar = input("¿Desea abrir el gestor interactivo de múltiples bibliotecas? (s/n): ").strip().lower()
    if activar == "s":
        menu_interactivo(b_personal, b_estudio)