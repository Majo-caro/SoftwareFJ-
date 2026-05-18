from Modelos.persona import Persona

class Cliente(Persona):

    def __init__(
        self,
        nombre,
        identificacion,
        correo
    ):

        super().__init__(
            nombre,
            identificacion
        )

        if "@" not in correo:

            raise ValueError(
                "Correo inválido"
            )

        self.__correo = correo

    def get_correo(self):
        return self.__correo

    def mostrar_info(self):

        return f"""
===================================
Nombre:
{self.get_nombre()}

Identificación:
{self.get_identificacion()}

Correo:
{self.__correo}
===================================
        """