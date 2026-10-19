#Escriba un programa que permita al usuario ingresar un texto y luego cuente y muestre la cantidad de palabras que contiene ese texto.
#El programa debe manejar la entrada de datos y formatear la salida de manera clara.

#Ingresamos texto
texto = input("Ingrese un texto: ")

#Separamos el texto en palabras y contamos la cantidad de palabras
palabras = texto.split()
cantidad_palabras = len(palabras)

#Mostramos resultado
print(f"El texto ingresado contiene {cantidad_palabras} palabras.")

