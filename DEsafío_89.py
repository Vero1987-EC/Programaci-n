import os

def eliminar_prestamo(nombre_archivo):
    # Crear archivo de prueba si no existe
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("Juan Pérez - El principito - 10/10/2026\n")
            f.write("María Gómez - 1984 - 12/10/2026\n")
            f.write("Carlos López - Rayuela - 15/10/2026\n")

    try:
        # 1. Leer todas las líneas del archivo
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("⚠️ El archivo de préstamos está vacío.")
            return

        # 2. Mostrar los registros numerados
        print("\n📋 === REGISTROS ACTUALES DE PRÉSTAMOS ===")
        for i, linea in enumerate(lineas, 1):
            print(f"{i}. {linea.strip()}")

        # 3. Solicitar al usuario el número a eliminar
        opcion = int(input("\nIngrese el número del registro que desea eliminar: "))

        if 1 <= opcion <= len(lineas):
            registro_eliminado = lineas.pop(opcion - 1)
            
            # 4. Reescribir el archivo sin la línea eliminada
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.writelines(lineas)
                
            print(f"\n✅ Registro eliminado con éxito: '{registro_eliminado.strip()}'")
        else:
            print("❌ Número de opción inválido.")

    except ValueError:
        print("❌ Error: Debe ingresar un número entero válido.")
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no existe.")

if __name__ == "__main__":
    eliminar_prestamo("prestamos.txt")