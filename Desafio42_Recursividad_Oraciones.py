def invertir_palabras_recursivo(lista_palabras):
    # 1. CASO BASE: Si la lista está vacía o tiene un solo elemento, ya está "invertida"
    if len(lista_palabras) <= 1:
        return lista_palabras
    
    # 2. CASO RECURSIVO: Tomamos la última palabra de la lista (lista_palabras[-1])
    # y la unimos al principio de la inversión recursiva del resto de la lista (lista_palabras[:-1])
    return [lista_palabras[-1]] + invertir_palabras_recursivo(lista_palabras[:-1])

def invertir_oracion(oracion):
    # Separamos la oración en palabras. .split() sin argumentos elimina automáticamente 
    # múltiples espacios consecutivos y maneja la puntuación adyacente a las palabras.
    palabras = oracion.split()
    
    # Llamamos a nuestra función recursiva para invertir la lista de palabras
    palabras_invertidas = invertir_palabras_recursivo(palabras)
    
    # Unimos las palabras invertidas en una sola cadena de texto usando un único espacio
    return " ".join(palabras_invertidas)

# --- Entrada dinámica de datos (Interactiva) ---
print("--- INVERSOR RECURSIVO DE PALABRAS ---")
oracion_usuario = input("Ingrese una oración: ")

# Validamos que no esté vacía
if oracion_usuario.strip() == "":
    print("Por favor, ingrese una oración válida.")
else:
    resultado = invertir_oracion(oracion_usuario)
    print(f"\nOración original: '{oracion_usuario}'")
    print(f"Oración invertida: '{resultado}'")