
def realizar_division():
    try:
        # Solicitud de datos al usuario
        num1 = int(input("Ingrese el primer número entero (dividendo): "))
        num2 = int(input("Ingrese el segundo número entero (divisor): "))

        # Operación de división
        resultado = num1 / num2

    except ValueError:
        # Captura errores cuando la entrada no se puede convertir a entero
        print("Error: Debe ingresar únicamente números enteros válidos.")
    except ZeroDivisionError:
        # Captura el intento de dividir por cero
        print("Error: No es posible dividir por cero.")
    else:
        # Se ejecuta únicamente si no ocurrió ninguna excepción
        print(f"Resultado de la división ({num1} / {num2}): {resultado:.2f}")


def main():
    print("Manejo de Excepciones - División Segura")
    print("-" * 40)
    realizar_division()
    print("-" * 40)


if __name__ == "__main__":
    main()