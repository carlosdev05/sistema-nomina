from modelos.empleado import Empleado


class EmpleadoPorHoras(Empleado):
    """
    Empleado cuyo salario depende de las horas trabajadas.

    Las primeras 40 horas se pagan normalmente.
    Las horas adicionales se pagan a 1.5 veces la tarifa.
    """

    HORAS_NORMALES = 40
    FACTOR_HORA_EXTRA = 1.5
    FONDO_AHORRO = 0.02

    def __init__(
        self,
        nombre,
        identificacion,
        tarifa_hora,
        horas_trabajadas,
        años_empresa,
        acepta_fondo
    ):
        super().__init__(nombre, identificacion)

        if tarifa_hora < 0:
            raise ValueError("La tarifa por hora no puede ser negativa.")

        if horas_trabajadas < 0:
            raise ValueError("Las horas trabajadas no pueden ser negativas.")

        if años_empresa < 0:
            raise ValueError("Los años en la empresa no pueden ser negativos.")

        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas
        self.años_empresa = años_empresa
        self.acepta_fondo = acepta_fondo

    def calcular_salario_bruto(self):
        horas_normales = min(
            self.horas_trabajadas,
            self.HORAS_NORMALES
        )

        horas_extra = max(
            self.horas_trabajadas - self.HORAS_NORMALES,
            0
        )

        pago_normal = horas_normales * self.tarifa_hora

        pago_extra = (
            horas_extra
            * self.tarifa_hora
            * self.FACTOR_HORA_EXTRA
        )

        return pago_normal + pago_extra

    def calcular_fondo_ahorro(self):
        if self.años_empresa > 1 and self.acepta_fondo:
            return self.calcular_salario_bruto() * self.FONDO_AHORRO

        return 0

    def obtener_tipo(self):
        return "Por Horas"

    def obtener_beneficios(self):
        return 0