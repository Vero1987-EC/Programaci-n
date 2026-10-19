#Escribir un programa que solicite al usuario que ingrese una cantidad de dinero en su moneda local y luego convierta esa cantidad a otra moneda.
#Usando tasas de cambio proporcionada. El programa debe manejar la entrada de datos y formatear la salida de manera clasra.

#Ingreso de datos
monto_local = float(input("Ingrese la cantidad de dinero en su moneda local: "))
tasa_cambio = float(input("Ingrese la tasa de cambio (1 unidad de su moneda local = X unidades de la otra moneda): "))

#Conversion de moneda
monto_convertido = monto_local * tasa_cambio

#Mostramos resultado
print(f"{monto_local:.2f} en su moneda local equivale a {monto_convertido:.2f} en la otra moneda.")
