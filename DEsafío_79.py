
class NodoABB:

  def __init__(self, key):
    self.val = key
    self.izq = None
    self.der = None


def insertar(raiz, clave):
  if raiz is None:
    return NodoABB(clave)
  if clave < raiz.val:
    raiz.izq = insertar(raiz.izq, clave)
  elif clave > raiz.val:
    raiz.der = insertar(raiz.der, clave)
  return raiz


def buscar(raiz, clave):
  if raiz is None:
    return False
  if raiz.val == clave:
    return True
  return buscar(raiz.izq, clave) if clave < raiz.val else buscar(raiz.der, clave)


def main():
  numeros = [15, 8, 23, 3, 11, 18, 27]
  raiz = None
  for num in numeros:
    raiz = insertar(raiz, num)

  print("Buscar 11:", "Encontrado" if buscar(raiz, 11) else "No encontrado")
  print("Buscar 99:", "Encontrado" if buscar(raiz, 99) else "No encontrado")


if __name__ == "__main__":
  main()
