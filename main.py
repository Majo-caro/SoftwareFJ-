# =========================================
# MAIN PRINCIPAL
# =========================================

# Importamos clases
from Modelos.cliente import Cliente

from Modelos.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from Modelos.reserva import Reserva

from Utils.logger import registrar_log

# =========================================
# LISTAS DEL SISTEMA
# =========================================

clientes = []
reservas = []
servicios = []

# =========================================
# CLIENTES
# =========================================

print("\n===== CLIENTES =====\n")

try:

    # Cliente válido
    cliente1 = Cliente(
        "Maria",
        "101",
        "maria@gmail.com"
    )

    clientes.append(cliente1)

    print(
        "Cliente registrado"
    )

except Exception as error:

    registrar_log(error)

# =========================================
# CLIENTE INVÁLIDO
# =========================================

try:

    cliente2 = Cliente(
        "Pedro",
        "102",
        "correo_mal"
    )

    clientes.append(cliente2)

except Exception as error:

    registrar_log(error)

    print(
        "Error cliente inválido"
    )

# =========================================
# SERVICIOS
# =========================================

print("\n===== SERVICIOS =====\n")

try:

    sala = ReservaSala(
        "Sala VIP",
        100,
        5
    )

    equipo = AlquilerEquipo(
        "Laptop Gamer",
        80,
        3
    )

    asesoria = (
        AsesoriaEspecializada(
            "IA Empresarial",
            200,
            "Avanzado"
        )
    )

    servicios.append(sala)
    servicios.append(equipo)
    servicios.append(asesoria)

    print(
        "Servicios creados"
    )

except Exception as error:

    registrar_log(error)

# =========================================
# POLIMORFISMO
# =========================================

print("\n===== POLIMORFISMO =====\n")

for servicio in servicios:

    print(
        servicio.descripcion()
    )

    print(
        servicio.calcular_costo()
    )

# =========================================
# RESERVA EXITOSA
# =========================================

print("\n===== RESERVA EXITOSA =====\n")

try:

    reserva1 = Reserva(
        cliente1,
        sala,
        5
    )

    reservas.append(reserva1)

    reserva1.confirmar()

    reserva1.procesar()

except Exception as error:

    registrar_log(error)

# =========================================
# RESERVA FALLIDA
# =========================================

print("\n===== RESERVA FALLIDA =====\n")

try:

    reserva2 = Reserva(
        cliente1,
        equipo,
        -2
    )

    reservas.append(reserva2)

    reserva2.confirmar()

    reserva2.procesar()

except Exception as error:

    registrar_log(error)

# =========================================
# MOSTRAR RESERVAS
# =========================================

print("\n===== LISTA RESERVAS =====\n")

for reserva in reservas:

    print(
        f"""
        Cliente:
        {reserva.cliente.get_nombre()}

        Estado:
        {reserva.estado}
        """
    )

print(
    "\nSistema ejecutado correctamente"
)