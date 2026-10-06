from modelos.empleado import Empleado


class EmpleadoPorComision(Empleado):
    """
    Empleado con salario base más comisión sobre ventas.

    Si las ventas superan $20.000.000:
    recibe un bono adicional del 3% sobre las ventas.
    """

    PORCENTAJE_COMISION = 0.05
    LIMITE_BONO = 20_000_000
    BONO_VENTAS = 0.03
    BONO_ALIMENTACION = 1_000_000

    def __init__(
        self,
        nombre,
        identificacion,
        salario_base,
        ventas
    ):
        super().__init__(nombre, identificacion)

        if salario_base < 0:
            raise ValueError("El salario base no puede ser negativo.")

        if ventas < 0:
            raise ValueError("Las ventas no pueden ser negativas.")

        self.salario_base = salario_base
        self.ventas = ventas

    def calcular_comision(self):
        return self.ventas * self.PORCENTAJE_COMISION

    def calcular_bono_ventas(self):
        if self.ventas > self.LIMITE_BONO:
            return self.ventas * self.BONO_VENTAS

        return 0

    def calcular_salario_bruto(self):
        return (
            self.salario_base
            + self.calcular_comision()
            + self.calcular_bono_ventas()
        )

    def obtener_tipo(self):
        return "Por Comisión"

    def obtener_beneficios(self):
        return self.BONO_ALIMENTACION