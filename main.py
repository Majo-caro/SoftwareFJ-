import json
import os

from Modelos.cliente import Cliente

from Modelos.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from Modelos.reserva import Reserva

from Utils.logger import registrar_log

# =========================================
# LISTAS
# =========================================

clientes = []
reservas = []
servicios = []

# =========================================
# SERVICIOS
# =========================================

sala = ReservaSala(
    "Sala VIP",
    100
)

equipo = AlquilerEquipo(
    "Laptop Gamer",
    80
)

asesoria = AsesoriaEspecializada(
    "IA Empresarial",
    200,
    "Avanzado"
)

servicios.append(sala)
servicios.append(equipo)
servicios.append(asesoria)

# =========================================
# GUARDAR CLIENTES
# =========================================

def guardar_clientes():

    datos = []

    for cliente in clientes:

        datos.append({

            "nombre":
            cliente.get_nombre(),

            "identificacion":
            cliente.get_identificacion(),

            "correo":
            cliente.get_correo()
        })

    with open(
        "clientes.json",
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )

# =========================================
# GUARDAR RESERVAS
# =========================================

def guardar_reservas():

    datos = []

    for reserva in reservas:

        datos.append({

            "cliente":
            reserva.cliente.get_nombre(),

            "identificacion":
            reserva.cliente.get_identificacion(),

            "correo":
            reserva.cliente.get_correo(),

            "tipo_servicio":
            reserva.servicio.__class__.__name__,

            "servicio":
            reserva.servicio.nombre,

            "descripcion":
            reserva.servicio.descripcion(),

            "costo_base":
            reserva.servicio.costo_base,

            "duracion":
            reserva.duracion,

            "estado":
            reserva.estado
        })

    with open(
        "reservas.json",
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )

# =========================================
# CARGAR CLIENTES
# =========================================

def cargar_clientes():

    if os.path.exists(
        "clientes.json"
    ):

        try:

            with open(
                "clientes.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                contenido = archivo.read()

                if contenido.strip() == "":

                    return

                datos = json.loads(
                    contenido
                )

                for item in datos:

                    cliente = Cliente(

                        item["nombre"],
                        item["identificacion"],
                        item["correo"]
                    )

                    clientes.append(cliente)

        except Exception as error:

            registrar_log(error)

# =========================================
# CARGAR RESERVAS
# =========================================

def cargar_reservas():

    if os.path.exists(
        "reservas.json"
    ):

        try:

            with open(
                "reservas.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                contenido = archivo.read()

                if contenido.strip() == "":

                    return

                datos = json.loads(
                    contenido
                )

                for item in datos:

                    cliente_encontrado = None

                    for cliente in clientes:

                        if (

                            cliente
                            .get_identificacion()

                            ==

                            item[
                                "identificacion"
                            ]
                        ):

                            cliente_encontrado = cliente

                    servicio_encontrado = None

                    for servicio in servicios:

                        if (

                            servicio.nombre

                            ==

                            item["servicio"]
                        ):

                            servicio_encontrado = servicio

                    if (
                        cliente_encontrado
                        and
                        servicio_encontrado
                    ):

                        reserva = Reserva(

                            cliente_encontrado,

                            servicio_encontrado,

                            item["duracion"]
                        )

                        reserva.estado = item[
                            "estado"
                        ]

                        reservas.append(
                            reserva
                        )

        except Exception as error:

            registrar_log(error)

# =========================================
# INICIO
# =========================================

cargar_clientes()
cargar_reservas()

# =========================================
# MENÚ
# =========================================

while True:

    print("\n===================================")
    print("        SOFTWARE FJ")
    print("===================================")

    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Crear reserva")
    print("4. Mostrar reservas")
    print("5. Mostrar servicios")
    print("6. Cancelar reserva")
    print("7. Salir")

    opcion = input(
        "\nSeleccione opción: "
    )

    # =====================================
    # REGISTRAR CLIENTE
    # =====================================

    if opcion == "1":

        try:

            nombre = input(
                "Nombre: "
            )

            identificacion = input(
                "Identificación: "
            )

            correo = input(
                "Correo: "
            )

            cliente = Cliente(
                nombre,
                identificacion,
                correo
            )

            clientes.append(cliente)

            guardar_clientes()

            print(
                "\nCliente registrado"
            )

        except Exception as error:

            registrar_log(error)

            print(
                f"\nERROR: {error}"
            )

    # =====================================
    # MOSTRAR CLIENTES
    # =====================================

    elif opcion == "2":

        if len(clientes) == 0:

            print(
                "\nNo hay clientes"
            )

        else:

            for i, cliente in enumerate(
                clientes
            ):

                print(

                    f"""
===================================
CLIENTE #{i+1}

Nombre:
{cliente.get_nombre()}

Identificación:
{cliente.get_identificacion()}

Correo:
{cliente.get_correo()}
===================================
                    """
                )

    # =====================================
    # CREAR RESERVA
    # =====================================

    elif opcion == "3":

        try:

            if len(clientes) == 0:

                print(
                    "\nNo hay clientes registrados"
                )

                continue

            print("\n===== CLIENTES =====")

            for i, cliente in enumerate(
                clientes
            ):

                print(

                    f"{i+1}. "

                    f"{cliente.get_nombre()} "
                    f"- "
                    f"{cliente.get_identificacion()}"
                )

            opcion_cliente = int(

                input(
                    "\nSeleccione cliente: "
                )
            )

            cliente = clientes[
                opcion_cliente - 1
            ]

            print("\n===== SERVICIOS =====")

            for i, servicio in enumerate(
                servicios
            ):

                print(

                    f"{i+1}. "

                    f"{servicio.descripcion()}"
                )

            opcion_servicio = int(

                input(
                    "\nSeleccione servicio: "
                )
            )

            servicio = servicios[
                opcion_servicio - 1
            ]

            duracion = int(

                input(
                    "Duración del servicio: "
                )
            )

            # ================================
            # CREAR RESERVA
            # ================================

            reserva = Reserva(
                cliente,
                servicio,
                duracion
            )

            # ================================
            # VALIDAR RESERVA
            # ================================

            reserva.confirmar()

            # ================================
            # SOLO SI ES VÁLIDA
            # ================================

            reservas.append(
                reserva
            )

            reserva.procesar()

            guardar_reservas()

            print(
                "\nReserva creada correctamente"
            )

        except Exception as error:

            registrar_log(error)

            print(
                f"\nERROR: {error}"
            )

    # =====================================
    # MOSTRAR RESERVAS
    # =====================================

    elif opcion == "4":

        print("\n===== RESERVAS =====")

        if len(reservas) == 0:

            print(
                "\nNo hay reservas"
            )

        else:

            for i, reserva in enumerate(
                reservas
            ):

                print(

                    f"""
===================================
RESERVA #{i+1}

CLIENTE:
{reserva.cliente.get_nombre()}

SERVICIO:
{reserva.servicio.descripcion()}

DURACIÓN:
{reserva.duracion}

ESTADO:
{reserva.estado}

COSTO:
${reserva.servicio.calcular_costo(reserva.duracion)}
===================================
                    """
                )

    # =====================================
    # MOSTRAR SERVICIOS
    # =====================================

    elif opcion == "5":

        for i, servicio in enumerate(
            servicios
        ):

            print(

                f"""
-----------------------------------
SERVICIO #{i+1}

Descripción:
{servicio.descripcion()}

Costo base:
${servicio.costo_base}
-----------------------------------
                """
            )

    # =====================================
    # CANCELAR RESERVA
    # =====================================

    elif opcion == "6":

        try:

            if len(reservas) == 0:

                print(
                    "\nNo hay reservas"
                )

            else:

                print(
                    "\n===== RESERVAS ====="
                )

                for i, reserva in enumerate(
                    reservas
                ):

                    print(

                        f"""
{i+1}.

Cliente:
{reserva.cliente.get_nombre()}

Servicio:
{reserva.servicio.descripcion()}

Estado:
{reserva.estado}
                        """
                    )

                opcion_reserva = int(

                    input(
                        "\nSeleccione reserva a cancelar: "
                    )
                )

                reserva = reservas[
                    opcion_reserva - 1
                ]

                reserva.cancelar()

                guardar_reservas()

                print(
                    "\nReserva cancelada correctamente"
                )

        except Exception as error:

            registrar_log(error)

            print(
                f"\nERROR: {error}"
            )

    # =====================================
    # SALIR
    # =====================================

    elif opcion == "7":

        print(
            "\nSaliendo..."
        )

        break

    # =====================================
    # OPCIÓN INVÁLIDA
    # =====================================

    else:

        print(
            "\nOpción inválida"
        )