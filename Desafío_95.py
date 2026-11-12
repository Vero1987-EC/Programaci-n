def analisis_datos_ventas():
    # 1. Lista de ventas representadas mediante tuplas: (id_producto, cantidad, precio_unitario)
    ventas = [
        ("PROD_101", 5, 1200.0),
        ("PROD_102", 3, 2500.5),
        ("PROD_101", 10, 1200.0),
        ("PROD_103", 2, 4500.0),
        ("PROD_102", 7, 2500.5),
        ("PROD_101", 4, 1200.0)
    ]

    ingreso_total = 0.0
    unidades_por_producto = {}

    # 2. Iteración y desempaquetado de cada tupla de venta
    for id_producto, cantidad, precio_unitario in ventas:
        # Calcular el acumulado del ingreso total
        ingreso_total += cantidad * precio_unitario

        # Acumular la cantidad total de unidades vendidas por cada producto
        if id_producto in unidades_por_producto:
            unidades_por_producto[id_producto] += cantidad
        else:
            unidades_por_producto[id_producto] = cantidad

    # 3. Determinar el producto más vendido usando la función max() sobre el diccionario
    producto_mas_vendido = max(unidades_por_producto, key=unidades_por_producto.get)
    total_unidades = unidades_por_producto[producto_mas_vendido]

    # Mostrar resultados
    print(" === REPORTE DE ANÁLISIS DE VENTAS ===")
    print(f" Ingreso total generado: ${ingreso_total:,.2f}")
    print(f" Producto más vendido: {producto_mas_vendido} ({total_unidades} unidades)")

    print("\n Desglose total de unidades por producto:")
    for prod, cant in unidades_por_producto.items():
        print(f"   • {prod}: {cant} unidades")

if __name__ == "__main__":
    analisis_datos_ventas()