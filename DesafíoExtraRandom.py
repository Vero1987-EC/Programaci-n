import random

def lanzar_dados(cantidad_dados=2):
    # Caras de un dado estándar de 6 lados
    caras_dado = [1, 2, 3, 4, 5, 6]
    
    # random.choices permite repetición (reemplazo), simula lanzamientos independientes
    resultados = random.choices(caras_dado, k=cantidad_dados)
    return resultados

if __name__ == "__main__":
    # Lanzamos 2 dados
    dados = lanzar_dados(2)
    
    print(" === LANZAMIENTO DE DADOS DE JUEGO DE MESA ===")
    print(f"  • Dado 1: {dados[0]}")
    print(f"  • Dado 2: {dados[1]}")
    print(f"   Suma total: {sum(dados)}")
    
    # Verificación de dobles (si ambos dados sacan el mismo número)
    if dados[0] == dados[1]:
        print(" ¡Doble! Sacaste un par idéntico.")