def plataforma_educativa():
    # 1. Definimos el catálogo total de cursos ofrecidos por la plataforma
    todos_los_cursos = {"Python", "Bases de Datos", "Interfaces Web", "Ciencia de Datos"}

    # 2. Diccionario con clave: estudiante y valor: conjunto de cursos completados
    estudiantes_cursos = {
        "Ana": {"Python", "Bases de Datos", "Interfaces Web", "Ciencia de Datos"}, # Completó todos
        "Juan": {"Python", "Bases de Datos"},
        "María": {"Python"},                                                     # Solo completó Python
        "Pedro": {"Python", "Bases de Datos", "Interfaces Web", "Ciencia de Datos"}, # Completó todos
        "Lucía": {"Interfaces Web"},
        "Diego": {"Python"}                                                      # Solo completó Python
    }

    print(" === SISTEMA DE GESTIÓN DE PLATAFORMA EDUCATIVA ===\n")

    # -------------------------------------------------------------------------
    # Requisito 2: Estudiantes que completaron TODOS los cursos ofrecidos
    # -------------------------------------------------------------------------
    estudiantes_completos = []
    for estudiante, cursos in estudiantes_cursos.items():
        # Verificamos si el conjunto de cursos del estudiante es igual al total ofrecido
        if cursos == todos_los_cursos:
            estudiantes_completos.append(estudiante)

    print(f" Estudiantes que completaron TODOS los cursos ({len(estudiantes_completos)}):")
    for est in estudiantes_completos:
        print(f"   • {est}")

    # -------------------------------------------------------------------------
    # Requisito 3: Estudiantes que SOLO completaron un curso específico (ej. "Python")
    # -------------------------------------------------------------------------
    curso_especifico = "Python"
    solo_un_curso = []

    for estudiante, cursos in estudiantes_cursos.items():
        # Verificamos que tenga exactamente 1 curso registrado y que sea el buscado
        if len(cursos) == 1 and curso_especifico in cursos:
            solo_un_curso.append(estudiante)

    print(f"\n Estudiantes que completaron ÚNICAMENTE el curso '{curso_especifico}' ({len(solo_un_curso)}):")
    for est in solo_un_curso:
        print(f"   • {est}")

if __name__ == "__main__":
    plataforma_educativa()