class NodoExpresion:

  def __init__(self, val):
    self.val = val
    self.izq = None
    self.der = None


def evaluar_arbol(raiz):
  if raiz is None:
    return 0
  if raiz.izq is None and raiz.der is None:
    return int(raiz.val)

  val_izq = evaluar_arbol(raiz.izq)
  val_der = evaluar_arbol(raiz.der)

  if raiz.val == "+":
    return val_izq + val_der
  elif raiz.val == "-":
    return val_izq - val_der
  elif raiz.val == "*":
    return val_izq * val_der
  elif raiz.val == "/":
    return val_izq / val_der


def main():
  # Construcción para "5 + 3 * 4"
  raiz = NodoExpresion("+")
  raiz.izq = NodoExpresion("5")
  sub_der = NodoExpresion("*")
  sub_der.izq = NodoExpresion("3")
  sub_der.der = NodoExpresion("4")
  raiz.der = sub_der

  print("Resultado de '5 + 3 * 4':", evaluar_arbol(raiz))  # Resultado: 17


if __name__ == "__main__":
  main()