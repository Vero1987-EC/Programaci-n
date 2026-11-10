def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
    print("1. Agregar nuevo producto")
    print("2. Actualizar stock de un producto")
    print("3. Buscar producto por código")
    print("4. Ver inventario completo")
    print("5. Salir")

def sistema_inventario():
    # Diccionario principal: la clave es el código del producto
    inventario = {}

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-5): ").strip()

        if opcion == "1":
            # 1. Agregar nuevos productos
            codigo = input("Ingrese el código del producto: ").strip()
            
            if codigo in inventario:
                print(" Error: Ya existe un producto registrado con ese código.")
            else:
                nombre = input("Ingrese el nombre del producto: ").strip()
                try:
                    precio = float(input("Ingrese el precio: "))
                    stock = int(input("Ingrese la cantidad en stock: "))
                    
                    # Estructura de diccionario anidado
                    inventario[codigo] = {
                        "nombre": nombre,
                        "precio": precio,
                        "stock": stock
                    }
                    print(f" Producto '{nombre}' agregado exitosamente.")
                except ValueError:
                    print(" Error: El precio y el stock deben ser valores numéricos.")

        elif opcion == "2":
            # 2. Actualizar el stock de productos existentes
            codigo = input("Ingrese el código del producto a actualizar: ").strip()
            
            if codigo in inventario:
                try:
                    nuevo_stock = int(input(f"Ingrese el nuevo stock para '{inventario[codigo]['nombre']}': "))
                    inventario[codigo]["stock"] = nuevo_stock
                    print(f" Stock actualizado a {nuevo_stock} unidades.")
                except ValueError:
                    print(" Error: Debe ingresar un número entero válido para el stock.")
            else:
                print(" Producto no encontrado.")

        elif opcion == "3":
            # 3. Buscar productos por código y mostrar sus detalles
            codigo = input("Ingrese el código del producto a buscar: ").strip()
            
            if codigo in inventario:
                prod = inventario[codigo]
                print(f"\n--- DETALLES DEL PRODUCTO [{codigo}] ---")
                print(f" Nombre: {prod['nombre']}")
                print(f" Precio: ${prod['precio']:.2f}")
                print(f" Stock:  {prod['stock']} unidades")
            else:
                print(" Producto no encontrado.")

        elif opcion == "4":
            # Mostrar inventario completo
            if not inventario:
                print("\n El inventario está actualmente vacío.")
            else:
                print("\n=== LISTADO COMPLETO DE PRODUCTOS ===")
                for cod, detalles in inventario.items():
                    print(f"[{cod}] {detalles['nombre']} | Precio: ${detalles['precio']:.2f} | Stock: {detalles['stock']}")

        elif opcion == "5":
            print("¡Gracias por utilizar el sistema de inventario!")
            break
        else:
            print(" Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    sistema_inventario()