from Modelos.excepciones import ReservaError

from Utils.logger import registrar_log

class Reserva:

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
    # CONFIRMAR
    # =====================================

    def confirmar(self):

        # VALIDAR DURACIÓN

        if self.duracion <= 0:

            raise ReservaError(
                "Duración inválida"
            )

        self.estado = "Confirmada"

        registrar_log(
            "Reserva confirmada"
        )

        print(
            "\nReserva confirmada"
        )

    # =====================================
    # CANCELAR
    # =====================================

    def cancelar(self):

        self.estado = "Cancelada"

        registrar_log(
            "Reserva cancelada"
        )

    # =====================================
    # PROCESAR
    # =====================================

    def procesar(self):

        try:

            print(
                "\nProcesando reserva..."
            )

            costo = (
                self.servicio.calcular_costo(
                    self.duracion
                )
            )

            print(
                f"Costo total: ${costo}"
            )

        except Exception as error:

            registrar_log(error)

            print(
                f"\nERROR: {error}"
            )

        finally:

            print(
                "Proceso finalizado"
            )