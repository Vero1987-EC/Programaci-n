def operaciones_estudio_mercado():
    # 1. Conjuntos de encuestados por plataforma
    facebook = {"juan@1001.com", "maria@1001.com", "ana@1001.com", "pedro@1001.com", "carla@1001.com"}
    instagram = {"maria@1001.com", "ana@1001.com", "lucia@1001.com", "diego@1001.com", "carla@1001.com"}
    twitter = {"ana@1001.com", "pedro@1001.com", "lucia@1001.com", "roberto@1001.com", "carla@1001.com"}

    # -------------------------------------------------------------------------
    # Requisito 1: Usuarios que usan LAS TRES plataformas (Intersección triple)
    # -------------------------------------------------------------------------
    usan_tres = facebook.intersection(instagram, twitter)

    # -------------------------------------------------------------------------
    # Requisito 2: Usuarios que usan SOLO UNA plataforma (Diferencias exclusivas)
    # -------------------------------------------------------------------------
    solo_fb = facebook - instagram - twitter
    solo_ig = instagram - facebook - twitter
    solo_tw = twitter - facebook - instagram
    usan_solo_una = solo_fb.union(solo_ig, solo_tw)

    # -------------------------------------------------------------------------
    # Requisito 3: Usuarios que usan AL MENOS DOS plataformas
    # -------------------------------------------------------------------------
    fb_e_ig = facebook & instagram
    fb_y_tw = facebook & twitter
    ig_y_tw = instagram & twitter
    usan_al_menos_dos = fb_e_ig | fb_y_tw | ig_y_tw

    # Mostrar resultados
    print(" === ANÁLISIS DE ESTUDIO DE MERCADO ===\n")

    print(f"1️ Usan las TRES plataformas ({len(usan_tres)}):")
    for usuario in usan_tres:
        print(f"   • {usuario}")

    print(f"\n2️ Usan SOLO UNA plataforma ({len(usan_solo_una)}):")
    for usuario in usan_solo_una:
        print(f"   • {usuario}")

    print(f"\n3️ Usan AL MENOS DOS plataformas ({len(usan_al_menos_dos)}):")
    for usuario in usan_al_menos_dos:
        print(f"   • {usuario}")

if __name__ == "__main__":
    operaciones_estudio_mercado()