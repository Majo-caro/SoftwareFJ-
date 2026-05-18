from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(
        self,
        nombre,
        identificacion
    ):

        # =====================================
        # VALIDAR NOMBRE
        # =====================================

        if not nombre.replace(
            " ",
            ""
        ).isalpha():

            raise ValueError(
                "El nombre solo debe contener letras"
            )

        # =====================================
        # VALIDAR IDENTIFICACIÓN
        # =====================================

        if not identificacion.isdigit():

            raise ValueError(
                "La identificación debe ser numérica"
            )

        # =====================================
        # ATRIBUTOS PRIVADOS
        # =====================================

        self.__nombre = nombre
        self.__identificacion = identificacion

    # =========================================
    # GETTERS
    # =========================================

    def get_nombre(self):

        return self.__nombre

    def get_identificacion(self):

        return self.__identificacion

    # =========================================
    # SETTERS
    # =========================================

    def set_nombre(
        self,
        nombre
    ):

        if not nombre.replace(
            " ",
            ""
        ).isalpha():

            raise ValueError(
                "El nombre solo debe contener letras"
            )

        self.__nombre = nombre

    # =========================================
    # MÉTODO ABSTRACTO
    # =========================================

    @abstractmethod
    def mostrar_info(self):
        pass