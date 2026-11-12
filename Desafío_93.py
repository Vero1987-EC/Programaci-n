def traductor_multilingue(palabra_ingles, idiomas_solicitados, diccionario_traducciones):
    print(f" buscando traducciones para la palabra: '{palabra_ingles}'...")
    
    # 1. Verificar si la palabra en inglés existe en el diccionario principal
    if palabra_ingles not in diccionario_traducciones:
        print(f" La palabra '{palabra_ingles}' no se encuentra registrada en el diccionario.\n")
        return

    traducciones_disponibles = diccionario_traducciones[palabra_ingles]
    resultados = {}

    # 2. Iterar sobre la lista de idiomas solicitados
    for idioma in idiomas_solicitados:
        # Usamos .get() o try/except para capturar traducciones no disponibles
        traduccion = traducciones_disponibles.get(idioma)
        if traduccion:
            resultados[idioma] = traduccion
        else:
            resultados[idioma] = "Traducción no encontrada"

    # 3. Mostrar los resultados formateados
    print(" Resultados de la traducción:")
    for idioma, resultado in resultados.items():
        print(f"   • [{idioma.upper()}]: {resultado}")
    print()

if __name__ == "__main__":
    # Diccionario con clave principal en inglés y diccionario anidado para idiomas
    traducciones = {
        "hello": {
            "es": "hola",
            "fr": "bonjour",
            "pr": "olá",
            "it": "ciao",
            "de": "hallo"
        },
        "world": {
            "es": "mundo",
            "fr": "monde",
            "pr": "mundo",
            "it": "mondo",
            "de": "welt"
        },
        "computer": {
            "es": "computadora",
            "fr": "ordinateur",
            "it": "computer"
            # "de" y "pr" no están disponibles a propósito para probar el control de errores
        }
    }

    # Pruebas con diferentes combinaciones de idiomas
    idiomas_buscados = ["es", "fr", "it", "de", "ja"]  # 'ja' (japonés) no existe

    traductor_multilingue("hello", idiomas_buscados, traducciones)
    traductor_multilingue("computer", ["es", "de", "pr"], traducciones)
    traductor_multilingue("house", ["es", "fr"], traducciones)