def gestion_usuarios_concursos():
    # 1. Definimos las listas iniciales de participantes
    astronomia = ["ana@1001problemas.com", "juan@1001problemas.com", "maria@1001problemas.com", "pedro@1001problemas.com"]
    matematica = ["juan@1001problemas.com", "maria@1001problemas.com", "luis@1001problemas.com", "carla@1001problemas.com"]
    programacion = ["juan@1001problemas.com", "maria@1001problemas.com", "pedro@1001problemas.com", "lucia@1001problemas.com", "diego@1001problemas.com"]

    # 2. Convertimos las listas a conjuntos para realizar operaciones matemáticas
    set_astronomia = set(astronomia)
    set_matematica = set(matematica)
    set_programacion = set(programacion)

    # -------------------------------------------------------------------------
    # Requisito 1: Usuarios que participaron en TODOS los concursos (Intersección)
    # -------------------------------------------------------------------------
    en_todos = set_astronomia.intersection(set_matematica, set_programacion)
    
    # -------------------------------------------------------------------------
    # Requisito 2: Usuarios que SOLO participaron en "Programación" (Diferencia)
    # -------------------------------------------------------------------------
    solo_programacion = set_programacion.difference(set_astronomia, set_matematica)

    # -------------------------------------------------------------------------
    # Requisito 3: Todos los usuarios únicos (Unión de los tres conjuntos)
    # -------------------------------------------------------------------------
    todos_unicos = set_astronomia.union(set_matematica, set_programacion)

    # 3. Mostrar los resultados
    print(" === GESTIÓN DE USUARIOS EN CONCURSOS ===\n")

    print(f" Participaron en TODOS los concursos ({len(en_todos)}):")
    for usuario in en_todos:
        print(f"   • {usuario}")

    print(f"\n Participaron ÚNICAMENTE en 'Programación' ({len(solo_programacion)}):")
    for usuario in solo_programacion:
        print(f"   • {usuario}")

    print(f"\n TOTAL de usuarios únicos en al menos un concurso ({len(todos_unicos)}):")
    for usuario in todos_unicos:
        print(f"   • {usuario}")

if __name__ == "__main__":
    gestion_usuarios_concursos()