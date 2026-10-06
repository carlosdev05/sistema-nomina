from abc import ABC, abstractmethod


class Empleado(ABC):
    """
    Clase abstracta que representa un empleado.
    Define el comportamiento común para todos los empleados.
    """

    def __init__(self, nombre, identificacion):
        if not nombre.strip():
            raise ValueError("El nombre es obligatorio.")

        if not identificacion.strip():
            raise ValueError("La identificación es obligatoria.")

        self.nombre = nombre.strip()
        self.identificacion = identificacion.strip()

    @abstractmethod
    def calcular_salario_bruto(self):
        """Calcula el salario bruto del empleado."""
        pass

    @abstractmethod
    def obtener_tipo(self):
        """Retorna el tipo de empleado."""
        pass