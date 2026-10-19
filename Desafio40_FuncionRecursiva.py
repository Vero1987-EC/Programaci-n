def calcular_mcd(a, b):
    # Caso base: si b es 0, el MCD es a
    if b == 0:
        return a
    # Caso recursivo: se llama a sí misma con b y el residuo (a % b)
    else:
        return calcular_mcd(b, a % b)

# --- Entrada dinámica de datos ---
print("--- CALCULADORA DINÁMICA DE MCD ---")

# Solicitamos los números al usuario (al igual que en tus desafíos anteriores)
num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))

# Llamamos a la función y almacenamos el resultado
resultado = calcular_mcd(num1, num2)

# Presentamos el resultado de manera amigable usando f-strings
print(f"\nEl Máximo Común Divisor (MCD) de {num1} y {num2} es: {resultado}")