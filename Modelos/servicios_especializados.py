# =========================================
# SERVICIOS ESPECIALIZADOS
# =========================================

# Importamos Servicio
from Modelos.servicio import Servicio

# =========================================
# RESERVA DE SALAS
# =========================================

class ReservaSala(Servicio):

    # Constructor
    def __init__(self, nombre, costo_base, horas):

        super().__init__(
            nombre,
            costo_base
        )

        self.horas = horas

    # Polimorfismo
    def calcular_costo(self):

        return self.costo_base * self.horas

    # Descripción
    def descripcion(self):

        return (
            f"Reserva de sala por "
            f"{self.horas} horas"
        )

# =========================================
# ALQUILER EQUIPOS
# =========================================

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base, dias):

        super().__init__(
            nombre,
            costo_base
        )

        self.dias = dias

    # Polimorfismo
    def calcular_costo(self):

        return self.costo_base * self.dias

    def descripcion(self):

        return (
            f"Alquiler de equipo por "
            f"{self.dias} días"
        )

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

    # Polimorfismo
    def calcular_costo(self):

        # Validación nivel
        if self.nivel == "Avanzado":

            return self.costo_base * 2

        return self.costo_base

    def descripcion(self):

        return (
            f"Asesoría nivel "
            f"{self.nivel}"
        )