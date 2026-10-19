#Determinar su un numero es multiplo de otro, utilizando comparaciones y operadores logicos
#Crear un programa que dado un numero, verifique si esmultiplo de 2, 3, 5 , 7, 9, 10 y 11 mostrando un mensaje por cada caso
#Para cada uno de los numeros, el programa debe indicar si el numero es o no multiplo de estos.

#Ingresar un numero
numero = int(input("Ingrese un numero: "))

#Lista de numeros a verificar
numeros_a_verificar = [2, 3, 5, 7, 9, 10, 11]

#Verificar multiplos
for n in numeros_a_verificar:
    if numero % n == 0:
        print(f"{numero} es multiplo de {n}? Si")
    else:
        print(f"{numero} no es multiplo de {n}? No")
        