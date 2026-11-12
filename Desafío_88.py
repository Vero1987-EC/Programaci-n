import os

def eliminar_prestamo(nombre_archivo, numero_a_eliminar=None):
    # 1. Auto-crear el archivo de préstamos si no existe en la carpeta
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("Juan Pérez - El principito - 10/10/2026\n")
            f.write("María Gómez - 1984 - 12/10/2026\n")
            f.write("Carlos López - Rayuela - 15/10/2026\n")

    try:
        # 2. Leer las líneas actuales del archivo
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        if not lineas:
            print(" El archivo de préstamos está vacío.")
            return

        print("\n === REGISTROS ACTUALES DE PRÉSTAMOS ===")
        for i, linea in enumerate(lineas, 1):
            print(f"{i}. {linea.strip()}")

        # 3. Si no le pasamos un número explícito, se lo pedimos al usuario
        if numero_a_eliminar is None:
            entrada = input("\nIngrese el número de registro a eliminar: ").strip()
            if not entrada.isdigit():
                print(" Error: Debe ingresar un número válido.")
                return
            numero_a_eliminar = int(entrada)

        # 4. Validar el rango y eliminar la línea
        if 1 <= numero_a_eliminar <= len(lineas):
            eliminado = lineas.pop(numero_a_eliminar - 1)
            
            # Reescribir el archivo actualizado
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                f.writelines(lineas)
                
            print(f"\n ¡Éxito! Se eliminó el registro: '{eliminado.strip()}'")
        else:
            print(f"\n Error: El registro número {numero_a_eliminar} no existe.")

    except FileNotFoundError:
        print(f" Error: El archivo '{nombre_archivo}' no existe.")

if __name__ == "__main__":
    # Probamos eliminando directamente el registro 1 para verificar que todo funcione sin pedir datos por consola
    eliminar_prestamo("prestamos.txt", numero_a_eliminar=1)