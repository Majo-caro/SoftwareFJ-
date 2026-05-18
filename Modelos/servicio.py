# =========================================
# CLASE ABSTRACTA SERVICIO
# =========================================

# Importamos ABC
from abc import ABC, abstractmethod

# Clase abstracta
class Servicio(ABC):

    # Constructor
    def __init__(self, nombre, costo_base):

        self.nombre = nombre
        self.costo_base = costo_base

    # Método abstracto
    @abstractmethod
    def calcular_costo(self):
        pass

    # Método abstracto
    @abstractmethod
    def descripcion(self):
        pass