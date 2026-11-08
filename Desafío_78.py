
class Nodo:

  def __init__(self, key):
    self.val = key
    self.izq = None
    self.der = None


def maximo_postorden(raiz):
  """Recorre en postorden (Izq -> Der -> Raíz) y obtiene el valor máximo."""
  if raiz is None:
    return float("-inf")
  max_izq = maximo_postorden(raiz.izq)
  max_der = maximo_postorden(raiz.der)
  return max(max_izq, max_der, raiz.val)


def main():
  raiz = Nodo(10)
  raiz.izq = Nodo(5)
  raiz.der = Nodo(25)
  raiz.izq.izq = Nodo(2)
  raiz.izq.der = Nodo(18)
  raiz.der.izq = Nodo(12)
  raiz.der.der = Nodo(20)

  print("Valor máximo:", maximo_postorden(raiz))  


if __name__ == "__main__":
  main()
