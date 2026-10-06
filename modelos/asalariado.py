from modelos.empleado import Empleado


class EmpleadoAsalariado(Empleado):
    """
    Empleado con salario mensual fijo.

    Si tiene más de 5 años en la empresa:
    recibe un bono del 10% del salario.

    Además recibe el beneficio de alimentación.
    """

    BONO_ANTIGUEDAD = 0.10
    BONO_ALIMENTACION = 1_000_000

    def __init__(self, nombre, identificacion, salario, años_empresa):
        super().__init__(nombre, identificacion)

        if salario < 0:
            raise ValueError("El salario no puede ser negativo.")

        if años_empresa < 0:
            raise ValueError("Los años en la empresa no pueden ser negativos.")

        self.salario = salario
        self.años_empresa = años_empresa

    def calcular_salario_bruto(self):
        bono = 0

        if self.años_empresa > 5:
            bono = self.salario * self.BONO_ANTIGUEDAD

        return self.salario + bono

    def obtener_tipo(self):
        return "Asalariado"

    def obtener_beneficios(self):
        return self.BONO_ALIMENTACION