import os
import string
from collections import Counter

def palabras_mas_comunes(nombre_archivo, top_n=5):
    # Crear archivo de prueba si no existe
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("El principito es un libro maravilloso. El libro habla de un principito y su rosa. La rosa del principito es especial.\n")

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().lower()

        # Eliminar signos de puntuación (puntos, comas, etc.)
        for signo in string.punctuation:
            contenido = contenido.replace(signo, "")

        # Separar el texto en palabras individuales
        palabras = contenido.split()

        # Contar la frecuencia de cada palabra
        conteo = Counter(palabras)

        # Obtener las N palabras más comunes
        mas_comunes = conteo.most_common(top_n)

        print(f"\n🏆 === LAS {top_n} PALABRAS MÁS COMUNES EN '{nombre_archivo}' ===")
        for palabra, frecuencia in mas_comunes:
            print(f"  • '{palabra}': {frecuencia} veces")

    except FileNotFoundError:
        print(f" Error: El archivo '{nombre_archivo}' no existe.")

if __name__ == "__main__":
    palabras_mas_comunes("libros.txt", 5)