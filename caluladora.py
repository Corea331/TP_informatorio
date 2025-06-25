from tkinter import messagebox
from datosPersonales import personalDomestico

sueldosPorCategoria = {
    "A": 395253,  # Mensual sin retiro
    "B": 2897,    # Por hora hasta 23hs semanales
    "C": 355447,   # Mensual más 23hs semanales
}

# Los aportes inluyen jubilaión, obra social y ART
aportes = {
    "1" : 6816.05,      #Hasta 11 horas
    "2" : 10735.77,     #Desde 12 hasta 15 horas
    "3" : 28688.55,     #16 horas o más
}

def calcular_sueldo(empleado):
    