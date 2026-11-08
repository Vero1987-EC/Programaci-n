class Nodo:

  def __init__(self, key):
    self.val = key
    self.izq = None
    self.der = None


def print_preorder(raiz):
  """Recorrido en Preorden: Raíz -> Izquierda -> Derecha"""
  if raiz:
    print(raiz.val, end=" ")
    print_preorder(raiz.izq)
    print_preorder(raiz.der)


def main():
  print("--- DESAFÍO 76: RECORRIDO EN PREORDEN ---")

  # Construcción del árbol de 3 niveles
  #          10
  #        /    \
  #       5      15
  #      / \    /  \
  #     2   8  12   20
  raiz = Nodo(10)
  raiz.izq = Nodo(5)
  raiz.der = Nodo(15)
  raiz.izq.izq = Nodo(2)
  raiz.izq.der = Nodo(8)
  raiz.der.izq = Nodo(12)
  raiz.der.der = Nodo(20)

  print("Recorrido en Preorden:")
  print_preorder(raiz)
  print()


if __name__ == "__main__":
  main()