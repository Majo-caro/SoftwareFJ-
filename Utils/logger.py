# =========================================
# SISTEMA DE LOGS
# =========================================

# Importamos fecha
from datetime import datetime

# Función registrar logs
def registrar_log(mensaje):

    # Abrimos archivo logs
    with open(
        "logs.txt",
        "a",
        encoding="utf-8"
    ) as archivo:

        archivo.write(
            f"{datetime.now()} "
            f"-> {mensaje}\n"
        )