
def buscar_codigo(lista_codigos, codigo_buscado):
    """
    Busca la primera aparición de codigo_buscado en lista_codigos.
    Retorna el índice de posición si existe, o None en caso contrario.
    """
    codigo_clean = str(codigo_buscado).strip()

    # Verificación de pertenencia y obtención de índice
    if codigo_clean in lista_codigos:
        return lista_codigos.index(codigo_clean)
    return None


def main():
    print("--- DESAFÍO 72: BÚSQUEDA DE CÓDIGO EN INVENTARIO ---")
    print("-" * 60)

    # Lista predefinida de códigos en el inventario
    codigos_inventario = ["P101", "P205", "P310", "P450", "P500", "P620"]
    print(f" Lista de inventario: {codigos_inventario}")
    print("-" * 60)

    # Lectura interactiva por teclado
    codigo_usuario = input("Ingrese el código de producto a buscar: ").strip()

    posicion = buscar_codigo(codigos_inventario, codigo_usuario)

    if posicion is not None:
        print(f" El código '{codigo_usuario}' se encuentra en la posición (índice): {posicion}")
    else:
        print(f" El código '{codigo_usuario}' no se ha encontrado en la lista.")

    print("-" * 60)


if __name__ == "__main__":
    main()