#Escribir unprograma que defina variables enteras a y b. Utilizar el operador (%) para calcular el residuo de la división de a entre b. 
#Asegurarse que el programa maneje adecuadamente los casos en que b sea igual a cero, mostrando un mensaje de error en ese caso.

#Ingresar dos numeros
a=int(input("Ingrese un número entero a: "))
b=int(input("Ingrese un número entero b: "))

#Verificamos si b es cdero antes de calcular el módulo
if b == 0:
    print("Error: No se puede calcular el residuo de la división entre cero.")  
else:
    residuo = a % b
    print(f"El residuo de la división de {a} entre {b} es: {residuo}")  
    