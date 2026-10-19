#Dado 3 números enteros, el algoritmo debe determinar cuál es el mayor de los tres y mostrarlo en pantalla.
#Ingresamos los tres números enteros
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))        
c = int(input("Ingrese el tercer número: "))

#Clasificamos en orden ascendente y mostramos el mayor
if a <= b and a <= c:
    if b <= c:
        orden=[a, b, c]
    elif a <= c and c <= b:
        orden=[a, c, b]
    elif b <= a and a <= c:
        orden=[b, a, c]
    elif b <= c and c <= a:
        orden=[b, c, a]         
    elif c <= a and a <= b:
        orden=[c, a, b]
    else:
        orden=[c, b, a]

    print("Números en orden ascendente:", orden)

