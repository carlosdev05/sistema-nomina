from servicios.deducciones import CalculadoraDeducciones
from servicios.beneficios import CalculadoraBeneficios


class CalculadoraNomina:
    """
    Servicio encargado de calcular la nómina completa.
    """

    def __init__(self, porcentaje_arl=0.005):
        self.deducciones = CalculadoraDeducciones(porcentaje_arl)
        self.beneficios = CalculadoraBeneficios()

    def calcular(self, empleado):
        salario_bruto = empleado.calcular_salario_bruto()

        deducciones = self.deducciones.total_deducciones(
            salario_bruto
        )

        beneficios = self.beneficios.calcular(empleado)

        fondo_ahorro = 0

        if hasattr(empleado, "calcular_fondo_ahorro"):
            fondo_ahorro = empleado.calcular_fondo_ahorro()

        salario_neto = (
            salario_bruto
            + beneficios
            - deducciones
            - fondo_ahorro
        )

        if salario_neto < 0:
            raise ValueError(
                "El salario neto no puede ser negativo."
            )

        return {
            "nombre": empleado.nombre,
            "identificacion": empleado.identificacion,
            "tipo": empleado.obtener_tipo(),
            "salario_bruto": salario_bruto,
            "beneficios": beneficios,
            "deducciones": deducciones,
            "fondo_ahorro": fondo_ahorro,
            "salario_neto": salario_neto
        }