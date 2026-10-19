#Escribimos un algoritmo que calcula la suma de los primeros n números naturales
#Desde 1 hasta n, utilizando un bucle

#Pedimos al usuario que ingrese un número natural n
n= int(input("Ingrese un número natural n: "))

#Iniciamos la suma
suma = 0

#Sumamos los números del 1 hasta n
for i in range(1, n +1):
    suma += i

    #Mostramos el resultado
print(f"La suma de los primeros {n} números naturales es: {suma}")


