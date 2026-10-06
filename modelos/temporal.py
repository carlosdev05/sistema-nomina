from modelos.empleado import Empleado


class EmpleadoTemporal(Empleado):
    """
    Empleado con salario mensual fijo y contrato definido.

    No recibe bonos ni beneficios adicionales.
    """

    def __init__(
        self,
        nombre,
        identificacion,
        salario,
        duracion_contrato
    ):
        super().__init__(nombre, identificacion)

        if salario < 0:
            raise ValueError("El salario no puede ser negativo.")

        if duracion_contrato <= 0:
            raise ValueError(
                "La duración del contrato debe ser mayor que cero."
            )

        self.salario = salario
        self.duracion_contrato = duracion_contrato

    def calcular_salario_bruto(self):
        return self.salario

    def obtener_tipo(self):
        return "Temporal"

    def obtener_beneficios(self):
        return 0