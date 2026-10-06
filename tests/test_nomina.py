import unittest

from modelos.asalariado import EmpleadoAsalariado
from servicios.nomina import CalculadoraNomina


class TestCalculadoraNomina(unittest.TestCase):

    def test_calculo_nomina_completo(self):
        empleado = EmpleadoAsalariado(
            "Carlos",
            "1001",
            3_000_000,
            6
        )

        nomina = CalculadoraNomina(
            porcentaje_arl=0.005
        )

        resultado = nomina.calcular(empleado)

        self.assertEqual(
            resultado["salario_bruto"],
            3_300_000
        )

        self.assertEqual(
            resultado["beneficios"],
            1_000_000
        )

        self.assertEqual(
            resultado["deducciones"],
            148_500
        )

        self.assertEqual(
            resultado["salario_neto"],
            4_151_500
        )


if __name__ == "__main__":
    unittest.main()