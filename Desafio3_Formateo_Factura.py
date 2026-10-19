#Escriba un programa que pueda tomar los detalles de los productos (nombre, cantidad, precio) y produzca una factura bien formateada.
#Ingreso de datos de producto
producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad del producto: "))
precio = float(input("Ingrese el precio del producto: "))

#Calculo total
total = cantidad * precio

#Mostramos fatura
print("\nFactura")
print("----------------------------")       
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: ${precio:.2f}")
print(f"Total: ${total:.2f}")
