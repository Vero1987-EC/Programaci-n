def simulacion_climatica():
    # 1. Almacenamos registros climáticos inmutables: (ciudad, temperatura_°C, porcentaje_humedad)
    registros_clima = [
        ("Buenos Aires", 24.5, 65.0),
        ("Rosario", 28.2, 58.0),
        ("Córdoba", 31.0, 45.0),    # Temperatura más alta
        ("Bariloche", 12.4, 72.0),   # Temperatura más baja
        ("Mendoza", 26.8, 40.0),
        ("Montevideo", 22.0, 70.0)
    ]

    print(" === SIMULACIÓN CLIMÁTICA CON TUPLAS ===\n")

    # Mostrar todos los registros
    print(" Registros meteorológicos obtenidos:")
    for ciudad, temp, humedad in registros_clima:
        print(f"   • {ciudad}: {temp}°C | Humedad: {humedad}%")

    # 2. Determinar la ciudad con la temperatura más alta y más baja
    # max/min evalúan el elemento en el índice 1 de la tupla (la temperatura)
    registro_max_temp = max(registros_clima, key=lambda reg: reg[2])
    registro_min_temp = min(registros_clima, key=lambda reg: reg[2])

    # 3. Calcular el promedio general de humedad
    # Sumamos el campo humedad (índice 2) de cada tupla
    total_humedad = sum(reg[3] for reg in registros_clima)
    promedio_humedad = total_humedad / len(registros_clima)

    # Resultados
    print("\n--------------------------------------------------")
    print(f" Ciudad con mayor temperatura: {registro_max_temp} ({registro_max_temp[2]}°C)")
    print(f" Ciudad con menor temperatura: {registro_min_temp} ({registro_min_temp[2]}°C)")
    print(f" Promedio general de humedad:  {promedio_humedad:.2f}%")

if __name__ == "__main__":
    simulacion_climatica()