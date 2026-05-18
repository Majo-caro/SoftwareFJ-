# =========================================
# CLASE ABSTRACTA PERSONA
# =========================================

# Importamos ABC para crear clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta
class Persona(ABC):

    # Constructor
    def __init__(self, nombre, identificacion):

        # Encapsulación de atributos
        self.__nombre = nombre
        self.__identificacion = identificacion

    # Getter del nombre
    def get_nombre(self):
        return self.__nombre

    # Setter del nombre
    def set_nombre(self, nombre):

        # Validación
        if nombre == "":
            raise ValueError(
                "El nombre no puede estar vacío"
            )

        self.__nombre = nombre

    # Getter identificación
    def get_identificacion(self):
        return self.__identificacion

    # Método abstracto
    @abstractmethod
    def mostrar_info(self):
        pass