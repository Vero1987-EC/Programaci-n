import random

def generar_temperaturas_climaticas(cantidad):
    """
    Genera una lista de temperaturas aleatorias de punto flotante
    en el rango de -10.0 a 40.0 °C utilizando random.uniform().
    """
    # Lista para almacenar las temperaturas
    temperaturas = []
    
    for _ in range(cantidad):
        # random.uniform(a, b) genera un float aleatorio N tal que a <= N <= b
        temp = random.uniform(-10.0, 40.0)
        # Opcional: redondear a 2 decimales para mejor legibilidad
        temperaturas.append(round(temp, 2))
        
    return temperaturas

# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    # Cantidad de datos de temperatura a simular
    num_muestras = 10
    
    # Generar temperaturas
    datos_clima = generar_temperaturas_climaticas(num_muestras)
    
    # Mostrar los resultados
    print(f"=== SIMULACIÓN CLIMÁTICA: {num_muestras} TEMPERATURAS GENERADAS ===")
    for i, t in enumerate(datos_clima, 1):
        print(f"Muestra {i}: {t} °C")