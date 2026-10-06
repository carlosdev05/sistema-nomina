import unittest

from modelos.asalariado import EmpleadoAsalariado


class TestEmpleadoAsalariado(unittest.TestCase):

    def test_salario_sin_bono_por_antiguedad(self):
        empleado = EmpleadoAsalariado(
            "Carlos",
            "1001",
            3_000_000,
            5
        )

        self.assertEqual(
            empleado.calcular_salario_bruto(),
            3_000_000
        )

    def test_salario_con_bono_por_antiguedad(self):
        empleado = EmpleadoAsalariado(
            "Carlos",
            "1001",
            3_000_000,
            6
        )

        self.assertEqual(
            empleado.calcular_salario_bruto(),
            3_300_000
        )

    def test_beneficio_alimentacion(self):
        empleado = EmpleadoAsalariado(
            "Carlos",
            "1001",
            3_000_000,
            6
        )

        self.assertEqual(
            empleado.obtener_beneficios(),
            1_000_000
        )

    def test_salario_negativo(self):
        with self.assertRaises(ValueError):
            EmpleadoAsalariado(
                "Carlos",
                "1001",
                -3_000_000,
                6
            )


if __name__ == "__main__":
    unittest.main()