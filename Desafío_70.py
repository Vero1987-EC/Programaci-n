
import math


# 1. Definición de la excepción personalizada
class NegativeNumberError(Exception):
    """Excepción lanzada cuando se intenta ingresar un número negativo."""

    def __init__(
        self,
        mensaje="No se puede calcular la raíz cuadrada de un número negativo.",
    ):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


# 2. Función principal con control de excepciones
def calcular_raiz_cuadrada():
    try:
        entrada = float(
            input("Ingrese un número para calcular su raíz cuadrada: ")
        )

        # Validación del dominio matemático
        if entrada < 0:
            raise NegativeNumberError("Error: El número ingresado es negativo.")

        resultado = math.sqrt(entrada)

    except ValueError:
        print("Error: Debe ingresar un valor numérico válido.")
    except NegativeNumberError as e:
        print(e)
    else:
        print(f"La raíz cuadrada de {entrada} es: {resultado:.2f}")


def main():
    print("Cálculo de Raíz Cuadrada con Excepción Personalizada")
    print("-" * 50)
    calcular_raiz_cuadrada()
    print("-" * 50)


if __name__ == "__main__":
    main()