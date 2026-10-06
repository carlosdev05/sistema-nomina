class CalculadoraDeducciones:
    """
    Calcula las deducciones obligatorias de la nómina.
    """

    PORCENTAJE_SEGURIDAD_PENSION = 0.04

    def __init__(self, porcentaje_arl=0.005):
        self.porcentaje_arl = porcentaje_arl

    def seguridad_social_pension(self, salario_bruto):
        return salario_bruto * self.PORCENTAJE_SEGURIDAD_PENSION

    def arl(self, salario_bruto):
        return salario_bruto * self.porcentaje_arl

    def total_deducciones(self, salario_bruto):
        return (
            self.seguridad_social_pension(salario_bruto)
            + self.arl(salario_bruto)
        )