#Contamos cuantos números pares hay en una lista dada, usamos % para verificar si cada número es divisble por 2.

#Lista de ejemplo
numeros = [1, 5, 3, 47, 50, 61, 76, 84, 9, 10]

#Inicializamos el contador
cantidad_pares = 0

#Recorremos la lista
for numero in numeros:
    #Verificamos si el número es par
    if numero % 2 == 0:
        cantidad_pares += 1

#Mostramos el resultado
print(f"La cantidad de números pares en la lista es: {cantidad_pares}")