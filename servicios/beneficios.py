class CalculadoraBeneficios:
    """
    Centraliza los beneficios adicionales de los empleados.
    """

    def calcular(self, empleado):
        if hasattr(empleado, "obtener_beneficios"):
            return empleado.obtener_beneficios()

        return 0