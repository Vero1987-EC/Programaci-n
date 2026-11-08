class Nodo:

  def __init__(self, key):
    self.val = key
    self.izq = None
    self.der = None


def sumar_inorden(raiz):
  """Recorre en inorden (Izq -> Raíz -> Der) y acumula la suma de nodos."""
  if raiz is None:
    return 0
  return sumar_inorden(raiz.izq) + raiz.val + sumar_inorden(raiz.der)


def main():
  raiz = Nodo(10)
  raiz.izq = Nodo(5)
  raiz.der = Nodo(15)
  raiz.izq.izq = Nodo(2)
  raiz.izq.der = Nodo(8)
  raiz.der.izq = Nodo(12)
  raiz.der.der = Nodo(20)

  print("Suma total de nodos:", sumar_inorden(raiz))  # Resultado: 72


if __name__ == "__main__":
  main()