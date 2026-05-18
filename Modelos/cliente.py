# =========================================
# CLASE CLIENTE
# =========================================

# Importamos Persona
from Modelos.persona import Persona

# Clase Cliente hereda de Persona
class Cliente(Persona):

    # Constructor
    def __init__(self, nombre, identificacion, correo):

        # Llamamos constructor padre
        super().__init__(
            nombre,
            identificacion
        )

        # Validamos correo
        if "@" not in correo:

            raise ValueError(
                "Correo inválido"
            )

        # Encapsulación
        self.__correo = correo

    # Getter correo
    def get_correo(self):
        return self.__correo

    # Método sobrescrito
    def mostrar_info(self):

        return f"""
        Nombre: {self.get_nombre()}
        ID: {self.get_identificacion()}
        Correo: {self.__correo}
        """