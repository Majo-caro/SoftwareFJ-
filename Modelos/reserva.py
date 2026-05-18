# =========================================
# CLASE RESERVA
# =========================================

# Importamos excepciones
from Modelos.excepciones import ReservaError

# Importamos logger
from Utils.logger import registrar_log

# Clase Reserva
class Reserva:

    # Constructor
    def __init__(
        self,
        cliente,
        servicio,
        duracion
    ):

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # =====================================
    # CONFIRMAR RESERVA
    # =====================================

    def confirmar(self):

        try:

            # Validación
            if self.duracion <= 0:

                raise ReservaError(
                    "Duración inválida"
                )

            # Cambio estado
            self.estado = "Confirmada"

            # Registrar evento
            registrar_log(
                "Reserva confirmada"
            )

            print(
                "Reserva confirmada"
            )

        except ReservaError as error:

            registrar_log(
                f"ERROR: {error}"
            )

            print(
                f"Error: {error}"
            )

    # =====================================
    # CANCELAR RESERVA
    # =====================================

    def cancelar(self):

        self.estado = "Cancelada"

        registrar_log(
            "Reserva cancelada"
        )

    # =====================================
    # PROCESAR RESERVA
    # =====================================

    def procesar(self):

        try:

            print(
                "\nProcesando reserva..."
            )

            costo = (
                self.servicio
                .calcular_costo()
            )

            print(
                f"Costo total: ${costo}"
            )

        except Exception as error:

            registrar_log(
                f"ERROR GENERAL: {error}"
            )

        finally:

            print(
                "Proceso finalizado\n"
            )