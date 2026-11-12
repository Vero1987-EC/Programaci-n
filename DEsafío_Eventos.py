def registro_eventos_inmutables():
    # 1. Lista de eventos representados mediante tuplas: (timestamp, usuario, acción)
    eventos = [
        ("2026-11-12 10:00:15", "usuario1@1001.com", "login"),
        ("2026-11-12 10:02:40", "usuario2@1001.com", "login"),
        ("2026-11-12 10:05:12", "usuario1@1001.com", "descarga_pdf"),
        ("2026-11-12 10:10:00", "usuario3@1001.com", "login"),
        ("2026-11-12 10:15:22", "usuario1@1001.com", "logout"),
        ("2026-11-12 10:20:05", "usuario2@1001.com", "descarga_pdf"),
        ("2026-11-12 10:25:30", "usuario3@1001.com", "modificar_perfil"),
        ("2026-11-12 10:30:00", "usuario2@1001.com", "logout")
    ]

    print(" === SISTEMA DE REGISTRO DE EVENTOS (LOGS) ===\n")

    # -------------------------------------------------------------------------
    # Requisito 2: Consultar eventos de un usuario específico
    # -------------------------------------------------------------------------
    usuario_buscar = "usuario1@1001.com"
    print(f" Eventos registrados para '{usuario_buscar}':")
    
    eventos_usuario = [evt for evt in eventos if evt[2] == usuario_buscar]
    
    if eventos_usuario:
        for timestamp, usuario, accion in eventos_usuario:
            print(f"   • [{timestamp}] Acción: '{accion}'")
    else:
        print("   No se encontraron eventos para este usuario.")

    # -------------------------------------------------------------------------
    # Requisito 3: Contar cuántas veces se realizó cada acción
    # -------------------------------------------------------------------------
    conteo_acciones = {}
    for timestamp, usuario, accion in eventos:
        if accion in conteo_acciones:
            conteo_acciones[accion] += 1
        else:
            conteo_acciones[accion] = 1

    print("\n--------------------------------------------------")
    print(" Conteo global de acciones realizadas:")
    for accion, total in conteo_acciones.items():
        print(f"   • {accion}: {total} vez/veces")

if __name__ == "__main__":
    registro_eventos_inmutables()