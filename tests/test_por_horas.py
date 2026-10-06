import unittest

from modelos.por_horas import EmpleadoPorHoras


class TestEmpleadoPorHoras(unittest.TestCase):

    def test_horas_normales(self):
        empleado = EmpleadoPorHoras(
            "Ana",
            "1002",
            20_000,
            40,
            2,
            False
        )

        self.assertEqual(
            empleado.calcular_salario_bruto(),
            800_000
        )

    def test_horas_extras(self):
        empleado = EmpleadoPorHoras(
            "Ana",
            "1002",
            20_000,
            45,
            2,
            False
        )

        esperado = (
            40 * 20_000
            + 5 * 20_000 * 1.5
        )

        self.assertEqual(
            empleado.calcular_salario_bruto(),
            esperado
        )

    def test_fondo_ahorro(self):
        empleado = EmpleadoPorHoras(
            "Ana",
            "1002",
            20_000,
            40,
            2,
            True
        )

        self.assertEqual(
            empleado.calcular_fondo_ahorro(),
            16_000
        )

    def test_no_recibe_fondo_si_no_lo_acepta(self):
        empleado = EmpleadoPorHoras(
            "Ana",
            "1002",
            20_000,
            40,
            2,
            False
        )

        self.assertEqual(
            empleado.calcular_fondo_ahorro(),
            0
        )

    def test_horas_negativas(self):
        with self.assertRaises(ValueError):
            EmpleadoPorHoras(
                "Ana",
                "1002",
                20_000,
                -5,
                2,
                False
            )


if __name__ == "__main__":
    unittest.main()