def registrar_prestamo():
    print("=== REGISTRO DE PRÉSTAMO DE LIBROS ===")
    
    # 1. Capturar la información del usuario
    libro = input("Ingrese el nombre del libro: ").strip()
    prestatario = input("Ingrese el nombre del prestatario: ").strip()
    fecha = input("Ingrese la fecha del préstamo (ej. DD/MM/AAAA): ").strip()
    
    # 2. Formatear la información del registro
    registro = f"Libro: {libro} | Prestatario: {prestatario} | Fecha: {fecha}\n"
    
    # 3. Guardar en el archivo prestamos.txt usando el modo de anexo ('a')
    with open("prestamos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(registro)
        
    print(" El préstamo se ha registrado correctamente en 'prestamos.txt'.")


# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    while True:
        registrar_prestamo()
        
        # Preguntar si desea agregar más registros
        respuesta = input("\n¿Deseas registrar otro préstamo? (s/n): ").strip().lower()
        if respuesta != 's':
            print("¡Programa finalizado!")
            break