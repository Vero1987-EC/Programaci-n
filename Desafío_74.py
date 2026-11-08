
from itertools import zip_longest


# OPCIÓN 1: Usando itertools.zip_longest (Recomendada y concisa)
def sumar_listas_zip(lista1, lista2):
    return [a + b for a, b in zip_longest(lista1, lista2, fillvalue=0)]


# OPCIÓN 2: Usando bucle for tradicional
def sumar_listas_bucle(lista1, lista2):
    resultado = []
    max_len = max(len(lista1), len(lista2))
    
    for i in range(max_len):
        val1 = lista1[i] if i < len(lista1) else 0
        val2 = lista2[i] if i < len(lista2) else 0
        resultado.append(val1 + val2)
        
    return resultado


def main():
    print("--- DESAFÍO 74: SUMA DE LISTAS DE DIFERENTE LONGITUD ---")
    print("-" * 65)

    lista_a = [10, 20, 30, 40, 50]
    lista_b = [5, 15, 25]

    resultado = sumar_listas_zip(lista_a, lista_b)

    print(f" Lista A ({len(lista_a)} elementos) : {lista_a}")
    print(f" Lista B ({len(lista_b)} elementos) : {lista_b}")
    print(f" Suma resultante         : {resultado}")
    print("-" * 65)


if __name__ == "__main__":
    main()