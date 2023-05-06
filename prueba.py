"""Probando la funcion para calcular la fecha de nacimiento."""

import datetime


def calcular_fecha(edad):
    "Usa la fecha actual menos la edad para hacer el calculo."
    fecha = datetime.date.today().year - edad
    print(fecha)


calcular_fecha(20)
