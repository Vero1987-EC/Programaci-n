
def main():
    print("--- DESAFÍO 75: POTENCIAS DE 2 CON LIST COMPREHENSION ---")
    print("-" * 65)

    # Definición de la lista mediante list comprehension (2^0 hasta 2^9)
    potencias = [2**i for i in range(10)]

    # Impresión de la lista resultante
    print(f"⚡ Lista 'potencias': {potencias}")
    print("-" * 65)

    # Detalle explicativo de cada término (opcional para revisión)
    for exponente, valor in enumerate(potencias):
        print(f"   2^{exponente} = {valor}")
    print("-" * 65)


if __name__ == "__main__":
    main()