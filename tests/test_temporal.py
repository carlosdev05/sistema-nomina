import unittest

from modelos.temporal import EmpleadoTemporal


class TestEmpleadoTemporal(unittest.TestCase):

    def test_salario_fijo(self):
        empleado = EmpleadoTemporal(
            "Laura",
            "1004",
            2_500_000,
            6
        )

        self.assertEqual(
            empleado.calcular_salario_bruto(),
            2_500_000
        )

    def test_no_tiene_beneficios(self):
        empleado = EmpleadoTemporal(
            "Laura",
            "1004",
            2_500_000,
            6
        )

        self.assertEqual(
            empleado.obtener_beneficios(),
            0
        )

    def test_duracion_contrato_invalida(self):
        with self.assertRaises(ValueError):
            EmpleadoTemporal(
                "Laura",
                "1004",
                2_500_000,
                0
            )

    def test_salario_negativo(self):
        with self.assertRaises(ValueError):
            EmpleadoTemporal(
                "Laura",
                "1004",
                -2_500_000,
                6
            )


if __name__ == "__main__":
    unittest.main()