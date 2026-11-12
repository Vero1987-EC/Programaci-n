import random

def realizar_sorteo(participantes, cantidad_ganadores):
    # Validamos que la cantidad solicitada no supere la cantidad de participantes
    if cantidad_ganadores > len(participantes):
        print(" Error: No se pueden seleccionar más ganadores que participantes.")
        return []

    # random.sample selecciona 'k' elementos sin repetición (únicos)
    ganadores = random.sample(participantes, cantidad_ganadores)
    return ganadores

if __name__ == "__main__":
    # Creamos una lista de 50 participantes para la prueba
    lista_participantes = [f"Participante_{i}" for i in range(1, 51)]
    
    # Seleccionamos 3 ganadores únicos para el sorteo
    ganadores_sorteo = realizar_sorteo(lista_participantes, 3)
    
    print(" === RESULTADOS DEL SORTEO ===")
    for i, ganador in enumerate(ganadores_sorteo, 1):
        print(f"   {i}° Premio: {ganador}")