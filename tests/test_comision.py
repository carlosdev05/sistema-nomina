import unittest

from modelos.comision import EmpleadoPorComision


class TestEmpleadoPorComision(unittest.TestCase):

    def test_calculo_de_comision(self):
        empleado = EmpleadoPorComision(
            "Pedro",
            "1003",
            2_000_000,
            10_000_000
        )

        self.assertEqual(
            empleado.calcular_comision(),
            500_000
        )

    def test_bono_por_superar_ventas(self):
        empleado = EmpleadoPorComision(
            "Pedro",
            "1003",
            2_000_000,
            25_000_000
        )

        self.assertEqual(
            empleado.calcular_bono_ventas(),
            750_000
        )

    def test_salario_bruto(self):
        empleado = EmpleadoPorComision(
            "Pedro",
            "1003",
            2_000_000,
            25_000_000
        )

        esperado = (
            2_000_000
            + 1_250_000
            + 750_000
        )

        self.assertEqual(
            empleado.calcular_salario_bruto(),
            esperado
        )

    def test_ventas_negativas(self):
        with self.assertRaises(ValueError):
            EmpleadoPorComision(
                "Pedro",
                "1003",
                2_000_000,
                -100
            )


if __name__ == "__main__":
    unittest.main()