from Modelos.servicio import Servicio

# =========================================
# RESERVA SALA
# =========================================

class ReservaSala(Servicio):

    def __init__(
        self,
        nombre,
        costo_base
    ):

        super().__init__(
            nombre,
            costo_base
        )

    def calcular_costo(
        self,
        duracion
    ):

        return (
            self.costo_base *
            duracion
        )

    def descripcion(self):

        return "Reserva Sala"

# =========================================
# ALQUILER EQUIPO
# =========================================

class AlquilerEquipo(Servicio):

    def __init__(
        self,
        nombre,
        costo_base
    ):

        super().__init__(
            nombre,
            costo_base
        )

    def calcular_costo(
        self,
        duracion
    ):

        return (
            self.costo_base *
            duracion
        )

    def descripcion(self):

        return "Alquiler Equipo"

# =========================================
# ASESORÍA ESPECIALIZADA
# =========================================

class AsesoriaEspecializada(Servicio):

    def __init__(
        self,
        nombre,
        costo_base,
        nivel
    ):

        super().__init__(
            nombre,
            costo_base
        )

        self.nivel = nivel

    def calcular_costo(
        self,
        duracion
    ):

        if self.nivel == "Avanzado":

            return (

                self.costo_base *

                duracion *

                2
            )

        return (

            self.costo_base *

            duracion
        )

    def descripcion(self):

        return (
            f"Asesoría {self.nivel}"
        )