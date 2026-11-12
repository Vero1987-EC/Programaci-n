def analisis_deportivo():
    # 1. Definimos los conjuntos de atletas participantes por torneo
    torneo_verano = {"Lucía", "Mateo", "Sofía", "Joaquín", "Elena"}
    torneo_otono = {"Sofía", "Joaquín", "Gabriel", "Valentina"}
    torneo_invierno = {"Mateo", "Sofía", "Joaquín", "Elena", "Lucas"}

    print(" === ANÁLISIS DE PARTICIPACIÓN DEPORTIVA ===\n")

    # -------------------------------------------------------------------------
    # Requisito 1: Atletas que participaron en TODOS los torneos (Intersección)
    # -------------------------------------------------------------------------
    atletas_en_todos = torneo_verano.intersection(torneo_otono, torneo_invierno)

    # -------------------------------------------------------------------------
    # Requisito 2: Atletas que participaron EXCLUSIVAMENTE en un único torneo
    # -------------------------------------------------------------------------
    unicos_verano = torneo_verano - torneo_otono - torneo_invierno
    unicos_otono = torneo_otono - torneo_verano - torneo_invierno
    unicos_invierno = torneo_invierno - torneo_verano - torneo_otono
    
    atletas_exclusivos = unicos_verano.union(unicos_otono, unicos_invierno)

    # -------------------------------------------------------------------------
    # Requisito 3: Cantidad total de atletas ÚNICOS (Unión completa)
    # -------------------------------------------------------------------------
    todos_los_atletas = torneo_verano.union(torneo_otono, torneo_invierno)

    # Mostrar resultados
    print(f" Atletas que compitieron en TODOS los torneos ({len(atletas_en_todos)}):")
    for atleta in atletas_en_todos:
        print(f"   • {atleta}")

    print(f"\n Atletas que compitieron en UN ÚNICO torneo ({len(atletas_exclusivos)}):")
    for atleta in atletas_exclusivos:
        print(f"   • {atleta}")

    print(f"\n TOTAL de atletas únicos en la temporada: {len(todos_los_atletas)}")

if __name__ == "__main__":
    analisis_deportivo()