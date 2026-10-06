import unittest

from servicios.deducciones import CalculadoraDeducciones


class TestDeducciones(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculadoraDeducciones(
            porcentaje_arl=0.005
        )

    def test_seguridad_social_pension(self):
        resultado = self.calculadora.seguridad_social_pension(
            3_000_000
        )

        self.assertEqual(
            resultado,
            120_000
        )

    def test_arl(self):
        resultado = self.calculadora.arl(
            3_000_000
        )

        self.assertEqual(
            resultado,
            15_000
        )

    def test_total_deducciones(self):
        resultado = self.calculadora.total_deducciones(
            3_000_000
        )

        self.assertEqual(
            resultado,
            135_000
        )


if __name__ == "__main__":
    unittest.main()