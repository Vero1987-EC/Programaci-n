#Escriba un programa que pida al usuario que ingrese dos números y luego imprima la suma, la resta, la multiplicación y la división de esos números.

#Ingresamos dos numeros
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

#Realizamos las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
#Verificamos si se puede dividir 
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir por cero"
#Mostramos resultados
print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La división de {num1} y {num2} es: {division}")
