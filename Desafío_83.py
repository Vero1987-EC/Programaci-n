def busqueda_binaria_estudiantes(lista_estudiantes, estudiante_buscado):
    """
    Realiza una búsqueda binaria en una lista ordenada alfabéticamente.
    Retorna la posición (índice) si lo encuentra, o None si no está.
    """
    inicio = 0
    fin = len(lista_estudiantes) - 1
    
    # Normalizamos a minúsculas para comparar sin conflicto de mayúsculas/minúsculas
    buscado_clean = estudiante_buscado.strip().lower()
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        nombre_actual = lista_estudiantes[medio].strip().lower()
        
        if nombre_actual == buscado_clean:
            return medio  # Estudiante encontrado
        elif nombre_actual < buscado_clean:
            inicio = medio + 1  # Buscar en la mitad derecha (alfabéticamente posterior)
        else:
            fin = medio - 1     # Buscar en la mitad izquierda (alfabéticamente anterior)
            
    return None  # No se encontró en la lista


def buscar_estudiante(lista_estudiantes, estudiante_buscado):
    """Función auxiliar para mostrar el mensaje adecuado según el resultado."""
    posicion = busqueda_binaria_estudiantes(lista_estudiantes, estudiante_buscado)
    
    if posicion is not None:
        print(f" El estudiante '{estudiante_buscado}' fue encontrado en la posición {posicion + 1} (índice {posicion}).")
    else:
        print(f" El estudiante '{estudiante_buscado}' no se encuentra registrado en la lista de la clase.")


# --- EJEMPLO DE USO ---
if __name__ == "__main__":
    # La lista DEBE estar previamente ordenada alfabéticamente
    estudiantes = ["Ana", "Carlos", "Daniela", "Esteban", "Fernanda", "Gonzalo", "Lucía", "Mateo", "Sofía", "Valentina"]

    print("--- BÚSQUEDA BINARIA DE ESTUDIANTES ---")
    
    # Caso 1: Estudiante presente
    buscar_estudiante(estudiantes, "Fernanda")
    
    # Caso 2: Estudiante ausente
    buscar_estudiante(estudiantes, "Joaquín")