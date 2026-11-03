
class Producto:
    """Representa un producto individual dentro del inventario."""

    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - ${self.precio:,.2f} (Stock: {self.stock})"


class Empleado:
    """Representa a un empleado de una sucursal."""

    def __init__(self, legajo, nombre, puesto):
        self.legajo = legajo
        self.nombre = nombre
        self.puesto = puesto

    def __str__(self):
        return f"[{self.legajo}] {self.nombre} ({self.puesto})"


class Transaccion:
    """Representa una operación de venta realizada en una tienda."""

    def __init__(self, id_transaccion, producto, cantidad, empleado):
        self.id_transaccion = id_transaccion
        self.producto = producto
        self.cantidad = cantidad
        self.empleado = empleado
        self.monto_total = producto.precio * cantidad


class Tienda:
    """
    Representa una sucursal que encapsula y gestiona la composición
    de productos, empleados y transacciones.
    """

    def __init__(self, sucursal, direccion):
        self.sucursal = sucursal
        self.direccion = direccion
        self.productos = []
        self.empleados = []
        self.transacciones = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def registrar_venta(self, id_transaccion, codigo_producto, cantidad, legajo_empleado):
        # Búsqueda encapsulada del producto
        producto = next((p for p in self.productos if p.codigo == codigo_producto), None)
        if not producto:
            print(f"Error: Producto con código '{codigo_producto}' no encontrado.")
            return False

        # Validación de stock
        if producto.stock < cantidad:
            print(f"Error: Stock insuficiente para '{producto.nombre}'. Disponible: {producto.stock}.")
            return False

        # Búsqueda encapsulada del empleado
        empleado = next((e for e in self.empleados if e.legajo == legajo_empleado), None)
        if not empleado:
            print(f"Error: Empleado con legajo '{legajo_empleado}' no encontrado.")
            return False

        # Actualización de stock y registro de transacción
        producto.stock -= cantidad
        venta = Transaccion(id_transaccion, producto, cantidad, empleado)
        self.transacciones.append(venta)
        print(f"Venta registrada con éxito: {cantidad}x {producto.nombre} por ${venta.monto_total:,.2f} (Atendió: {empleado.nombre})")
        return True

    def calcular_valor_inventario(self):
        return sum(p.precio * p.stock for p in self.productos)

    def mostrar_resumen(self):
        print(f"\n--- Resumen de Sucursal: {self.sucursal} ---")
        print(f"Dirección: {self.direccion}")
        print(f"Empleados a cargo: {len(self.empleados)}")
        print(f"Productos en catálogo: {len(self.productos)}")
        print(f"Valor total del inventario: ${self.calcular_valor_inventario():,.2f}")
        print(f"Total de ventas realizadas: {len(self.transacciones)}")


def main():
    print("Gestión de Inventario y Sucursales - Demostración de Composición")
    print("-" * 65)

    # 1. Instanciación de la sucursal
    tienda_norte = Tienda("Sucursal Norte", "Av. Libertador 1234")

    # 2. Agregar empleados y productos
    tienda_norte.agregar_empleado(Empleado("E001", "Carlos Gómez", "Vendedor"))
    tienda_norte.agregar_empleado(Empleado("E002", "María López", "Supervisora"))

    tienda_norte.agregar_producto(Producto("P101", "Laptop 15'", 350000.0, 8))
    tienda_norte.agregar_producto(Producto("P102", "Mouse Inalámbrico", 12000.0, 25))

    # 3. Operaciones de venta
    tienda_norte.registrar_venta("T-001", "P101", 2, "E001")
    tienda_norte.registrar_venta("T-002", "P102", 5, "E001")

    # 4. Resumen general
    tienda_norte.mostrar_resumen()
    print("-" * 65)


if __name__ == "__main__":
    main()