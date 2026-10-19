#Crear un programa que lea 5 calificaciones y calcule sub promedio
#Lista para almacenar las calificaciones
calificaciones = []
#Pedimos 5 notasal usuario
for i in range(5):
    nota = float(input(f"Ingrese la calificación {i+1}: "))
    calificaciones.append(nota)

#Calculamos el promedio
promedio = sum(calificaciones) / len(calificaciones)

print("El promedio es:", round(promedio, 2))
