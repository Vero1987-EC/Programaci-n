def historial_medico_inmutable():
    # 1. Almacenamos registros médicos inmutables: (fecha, paciente, diagnostico)
    registros = [
        ("2026-01-10", "Carlos Gómez", "Gripe A"),
        ("2026-02-15", "María Rodríguez", "Hipertensión"),
        ("2026-03-01", "Carlos Gómez", "Faringitis"),
        ("2026-04-12", "Ana Martínez", "Gripe A"),
        ("2026-05-20", "Carlos Gómez", "Control Anual"),
        ("2026-06-05", "María Rodríguez", "Diabetes Tipo 2")
    ]

    print(" === SISTEMA DE HISTORIAL MÉDICO (TUPLAS INMUTABLES) ===\n")

    # -------------------------------------------------------------------------
    # Requisito 2: Consultar el historial completo de un paciente específico
    # -------------------------------------------------------------------------
    paciente_buscar = "Carlos Gómez"
    print(f" Historial médico completo para '{paciente_buscar}':")
    
    historial_paciente = [reg for reg in registros if reg[2] == paciente_buscar]

    if historial_paciente:
        for fecha, paciente, diagnostico in historial_paciente:
            print(f"   • [{fecha}] Diagnóstico: {diagnostico}")
    else:
        print("   No se encontraron registros para este paciente.")

    # -------------------------------------------------------------------------
    # Requisito 3: Contar cuántos diagnósticos distintos se han registrado
    # -------------------------------------------------------------------------
    # Usamos un conjunto (set) para obtener los diagnósticos únicos
    diagnosticos_unicos = set(diagnostico for _, _, diagnostico in registros)

    print("\n--------------------------------------------------")
    print(f" Total de diagnósticos distintos registrados ({len(diagnosticos_unicos)}):")
    for diag in diagnosticos_unicos:
        print(f"   • {diag}")

if __name__ == "__main__":
    historial_medico_inmutable()