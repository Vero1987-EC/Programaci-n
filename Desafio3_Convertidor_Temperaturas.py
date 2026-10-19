#Analizar conversiones de tempeartura dada en Celsius a Fahrenheit y Kelvin utilizando operaciones directas sobre las variables.
#Ingresar temperatura en Celsius
celsius = float(input("Ingrese la temperatura en Celsius: "))

#Conversiones
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius}°C equivalen a {fahrenheit}°F y {kelvin}K")
