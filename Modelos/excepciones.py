# =========================================
# EXCEPCIONES PERSONALIZADAS
# =========================================

# Error personalizado reservas
class ReservaError(Exception):
    pass

# Error servicio no disponible
class ServicioNoDisponibleError(Exception):
    pass

# Error cliente inválido
class ClienteInvalidoError(Exception):
    pass