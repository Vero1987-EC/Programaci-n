

# =====================================================================
# CLASES DE COMPOSICIÓN (ROLES ADICIONALES)
# =====================================================================
class RolAdministrador:
    """Clase de composición que concede permisos administrativos."""

    def __init__(self, nivel_acceso="Estándar"):
        self.__nivel_acceso = nivel_acceso

    @property
    def nivel_acceso(self):
        return self.__nivel_acceso

    def gestionar_presupuesto(self, monto, departamento):
        print(f"🔑 [ADMIN {self.nivel_acceso}] Presupuesto de ${monto:,.2f} aprobado para {departamento}.")


class RolMantenimiento:
    """Clase de composición que otorga capacidades de mantenimiento informático/físico."""

    def __init__(self, especialidad_tecnica):
        self.__especialidad_tecnica = especialidad_tecnica

    @property
    def especialidad_tecnica(self):
        return self.__especialidad_tecnica

    def realizar_mantenimiento(self, equipo):
        print(f"🛠️ [MANTENIMIENTO {self.especialidad_tecnica}] Mantenimiento preventivo ejecutado en: {equipo}.")


# =====================================================================
# CLASES DE HERENCIA (EMPLEADOS Y SUBCLASES)
# =====================================================================
class Empleado:
    """Clase base encapsulada que representa a un Empleado general."""

    def __init__(self, nombre, id_empleado, salario, rol_adicional=None):
        self.__nombre = None
        self.__id_empleado = None
        self.__salario = None
        self.rol_adicional = rol_adicional  # COMPOSICIÓN

        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario = salario

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def id_empleado(self):
        return self.__id_empleado

    @id_empleado.setter
    def id_empleado(self, valor):
        if not isinstance(valor, (str, int)) or not str(valor).strip():
            raise ValueError("El ID no puede estar vacío.")
        self.__id_empleado = str(valor).strip()

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El salario debe ser un número no negativo.")
        self.__salario = float(valor)

    def mostrar_ficha(self):
        print(f"Empleado: {self.nombre} [ID: {self.id_empleado}] | Salario: ${self.salario:,.2f}")
        if self.rol_adicional:
            tipo_rol = type(self.rol_adicional).__name__
            print(f"   ↳ Rol Adicional (Composición): {tipo_rol}")


class Gerente(Empleado):
    """Subclase Gerente que hereda de Empleado."""

    def __init__(self, nombre, id_empleado, salario, departamento, rol_adicional=None):
        super().__init__(nombre, id_empleado, salario, rol_adicional)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    def tomar_decision(self, directiva):
        print(f"👔 [GERENCIA - {self.departamento}] {self.nombre} emitió la directiva: '{directiva}'.")

    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"   Cargo: Gerente | Departamento: {self.departamento}")


class Tecnico(Empleado):
    """Subclase Tecnico que hereda de Empleado."""

    def __init__(self, nombre, id_empleado, salario, area_tecnica, rol_adicional=None):
        super().__init__(nombre, id_empleado, salario, rol_adicional)
        self.__area_tecnica = area_tecnica

    @property
    def area_tecnica(self):
        return self.__area_tecnica

    def resolver_ticket(self, ticket_id):
        print(f"💻 [TÉCNICO - {self.area_tecnica}] {self.nombre} resolvió el ticket nº {ticket_id}.")

    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"   Cargo: Técnico | Área: {self.area_tecnica}")


class Voluntario(Empleado):
    """Subclase Voluntario (salario $0) con horas comunitarias."""

    def __init__(self, nombre, id_empleado, horas_donadas, rol_adicional=None):
        super().__init__(nombre, id_empleado, salario=0.0, rol_adicional=rol_adicional)
        self.horas_donadas = horas_donadas

    def mostrar_ficha(self):
        print(f"Voluntario: {self.nombre} [ID: {self.id_empleado}] | Horas Donadas: {self.horas_donadas} hs")
        if self.rol_adicional:
            tipo_rol = type(self.rol_adicional).__name__
            print(f"   ↳ Rol Adicional (Composición): {tipo_rol}")


def main():
    print("--- DEMOSTRACIÓN DESAFÍO 61: JERARQUÍA DE EMPLEADOS (HERENCIA Y COMPOSICIÓN) ---")
    print("-" * 75)

    # 1. Creación de Objetos de Roles (Composición)
    rol_admin = RolAdministrador(nivel_acceso="Total / Directivo")
    rol_mantenimiento = RolMantenimiento(especialidad_tecnica="Sistemas e Infraestructura")

    # 2. Instanciación de Empleados combinando Herencia y Composición
    gerente1 = Gerente(
        nombre="Dra. Beatriz Rossi",
        id_empleado="EMP-GER-01",
        salario=450000.0,
        departamento="Dirección General de Biblioteca",
        rol_adicional=rol_admin  # Composición
    )

    tecnico1 = Tecnico(
        nombre="Ing. Fernando Torres",
        id_empleado="EMP-TEC-05",
        salario=320000.0,
        area_tecnica="Base de Datos y Redes",
        rol_adicional=rol_mantenimiento  # Composición
    )

    voluntario1 = Voluntario(
        nombre="Sofia Martínez",
        id_empleado="VOL-2026-12",
        horas_donadas=40
    )

    # 3. Mostrar Fichas Técnicas
    print("📋 FICHAS DE EMPLEADOS:")
    gerente1.mostrar_ficha()
    print()
    tecnico1.mostrar_ficha()
    print()
    voluntario1.mostrar_ficha()
    print("-" * 75)

    # 4. Demostración de comportamientos heredados y compuestos
    print("⚡ EJECUCIÓN DE MÉTODOS HEREDADOS Y COMPUESTOS:")
    gerente1.tomar_decision("Apertura de la sala digital los sábados")
    if gerente1.rol_adicional:
        gerente1.rol_adicional.gestionar_presupuesto(1500000.0, gerente1.departamento)

    print()
    tecnico1.resolver_ticket("INC-9942 (Caída del catálogo online)")
    if tecnico1.rol_adicional:
        tecnico1.rol_adicional.realizar_mantenimiento("Servidor Principal de Búsquedas")

    print("-" * 75)


if __name__ == "__main__":
    main()